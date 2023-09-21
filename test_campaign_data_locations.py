"""This file contains tests to ensure all specified locations pass basic sanity checks.

Imports From:
    campaign.py
    report.py

Functions:
    test_campaign_data_locations()
"""
from campaign import Campaign
from report import Report


def test_campaign_data_locations(current_campaign: Campaign) -> Report:
    """Test all locations specified for sanity

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    player_bases: list[int] = []
    if current_campaign.campaign_data.parsed:
        for location in current_campaign.campaign_data.locations:
            if "PLAYER_BASE" in location.functions:
                player_bases.append(location.location_id)
                if location.alignment != "FRIENDLY":
                    report.errors.append(
                        f"ERROR: Location ID {location.location_id} is marked as "
                        "PLAYER BASE but is ENEMY alligned."
                    )

                if (
                    "INSERTION"
                    in current_campaign.campaign_data.player_mission_data["types"]
                ):
                    if "INSERTION" not in location.mission_types:
                        report.errors.append(
                            "ERROR: INSERTION mission type defined but player base location ID "
                            f"{location.location_id} does not specify "
                            "INSERTION as a valid MissionType."
                        )

                if (
                    "LAND_STRIKE"
                    in current_campaign.campaign_data.player_mission_data["types"]
                ):
                    if "LAND_STRIKE" not in location.mission_types:
                        report.errors.append(
                            "ERROR: LAND_STRIKE mission type defined but player base location ID "
                            f"{location.location_id} does not specify "
                            "LAND_STRIKE as a valid MissionType."
                        )

            if "LAND_STRIKE_TARGET" in location.functions:
                if f"LAND_STRIKE_LOCATION_{location.location_id}" not in [
                    mission.name for mission in current_campaign.missions
                ]:
                    report.errors.append(
                        f"ERROR: Location ID {location.location_id} specified as "
                        "LAND_STRIKE_TARGET but mission file LAND_STRIKE_LOCATION_"
                        f"{location.location_id} not found."
                    )

            if "INSERTION_TARGET" in location.functions:
                if f"INSERTION_LOCATION_{location.location_id}" not in [
                    mission.name for mission in current_campaign.missions
                ]:
                    report.errors.append(
                        f"ERROR: Location ID {location.location_id} specified as INSERTION_TARGET "
                        "but mission file INSERTION_LOCATION_{location.location_id} not found."
                    )

        if not player_bases:
            report.errors.append("ERROR: No location specified as PLAYER_BASE found.")
        elif len(player_bases) > 1:
            report.errors.append(
                "ERROR: More than one Location specified as PLAYER_BASE."
                f"Only one PLAYER_BASE may be specified: {player_bases}"
            )

        # Check SOSUS lines
        for location in current_campaign.campaign_data.locations:
            if not location.related_sosus:
                if "SOSUS_NODE" in location.functions:
                    report.warnings.append(
                        f"WARNING: Location ID {location.location_id} specified "
                        "as SOSUS_NODE but no related SOSUS found."
                    )
            else:
                if "SOSUS_NODE" not in location.functions:
                    report.warnings.append(
                        f"WARNING: Location ID {location.location_id} has related SOSUS lines "
                        f"{location.related_sosus} but not specified as SOSUS_NODE."
                    )
                for sosus_line in location.related_sosus:
                    if sosus_line not in [
                        sosus_line.name
                        for sosus_line in current_campaign.campaign_data.sosus_lines
                    ]:
                        report.errors.append(
                            f"ERROR: Location ID {location.location_id} has related SOSUS "
                            f"line {sosus_line} which is not a valid SOSUS line."
                        )

    return report
