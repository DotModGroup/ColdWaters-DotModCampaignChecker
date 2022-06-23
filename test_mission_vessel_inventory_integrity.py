"""This file contains tests to compare all vessels found in mission files to the vessel inventories

Imports From:
    campaign.py
    report.py

Functions:
    test_mission_vessel_inventory_integrity()
"""
from campaign import Campaign
from report import Report


def test_mission_vessel_inventory_integrity(current_campaign: Campaign) -> Report:
    """Test the vessels found in a mission for incorrect vessels and selectors

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    for mission in current_campaign.missions:
        mission_name = mission.name
        all_vessels: list[str] = []
        try:
            for index, vessel_role in enumerate(mission.enemy_units["classes"]):
                for vessel in vessel_role.split("|"):
                    all_vessels.append(vessel)
                    if mission.enemy_units["important"][index] == "TRUE":
                        if (
                            vessel
                            in current_campaign.vessel_inventory.vessel_inventory.keys()
                        ):
                            if (
                                current_campaign.vessel_inventory.vessel_inventory[
                                    vessel
                                ]
                                == 0
                                and len(vessel_role.split("|")) == 1
                            ):
                                report.infos.append(
                                    f"INFO: In mission {mission_name} critical vessel {vessel} "
                                    "has no units availible and so this mission cannot appear."
                                )
        except (KeyError, IndexError):
            continue
        for vessel in all_vessels:
            if (
                vessel not in current_campaign.vessel_inventory.vessel_inventory.keys()
                and vessel not in current_campaign.vessel_inventory.selectors.keys()
                and vessel != "testship"
            ):
                report.warnings.append(
                    f"WARNING: Mission {mission_name} has vessel {vessel}, "
                    "which is neither in the vessel inventory nor a valid selector."
                )
    return report
