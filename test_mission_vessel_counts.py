"""This file contains tests for vessel counts found in mission files

Imports From:
    campaign.py
    report.py

Functions:
    test_mission_vessel_counts()
"""
from campaign import Campaign
from report import Report


def test_mission_vessel_counts(current_campaign: Campaign):
    """Test the vessel counts in mission files for too many or too few vessels

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()
    for mission in current_campaign.missions:
        mission_name = mission.name
        max_vessel_count = 0
        min_vessel_count = 0
        min_critical_count = 0
        try:
            split_counts = [
                [count.split("-")[0], count.split("-")[1]]
                for count in mission.enemy_units["count"]
            ]
        except IndexError:
            continue
        for index, count in enumerate(split_counts):
            min_vessel_count += int(count[0])
            max_vessel_count += int(count[1])
            try:
                if mission.enemy_units["important"][index] == "TRUE":
                    min_critical_count += int(count[0])
            except (IndexError, KeyError):
                pass

        if min_vessel_count <= 0:
            report.warnings.append(
                f"WARNING: Mission {mission_name} has a minimum of {min_vessel_count} vessels."
            )

        if min_vessel_count > 10:
            report.warnings.append(
                f"WARNING: Mission {mission_name} has a maximum of {min_vessel_count} vessels."
            )

        if not current_campaign.campaign_data.parsed:
            return report

        if (
            min_critical_count <= 0
            and mission_name in current_campaign.campaign_data.player_missions
            and "testship" not in mission.enemy_units["classes"]
        ):
            report.warnings.append(
                f"WARNING: Mission {mission_name} has a minmum "
                f"of {min_critical_count} critical vessels."
            )
    return report
