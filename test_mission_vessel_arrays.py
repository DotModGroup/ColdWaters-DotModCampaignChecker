"""This file contains tests for the various vessel arrays found in mission files

Imports From:
    campaign.py
    report.py

Functions:
    test_mission_vessel_arrays()
"""
from campaign import Campaign
from report import Report


def test_mission_vessel_arrays(current_campaign: Campaign) -> Report:
    """Test the vessel arrays found in a mission for mismatched lengths

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()
    for mission in current_campaign.missions:
        mission_name = mission.name
        if mission.enemy_units["count"] != ["NONE"]:
            try:
                count = len(mission.enemy_units["count"])
                behavior = len(mission.enemy_units["behavior"])
                importance = len(mission.enemy_units["important"])
                classes = len(mission.enemy_units["classes"])
            except KeyError:
                if "RETURN_TO_BASE" not in mission_name:
                    if "count" not in mission.enemy_units.keys():
                        report.errors.append(
                            f"ERROR: Mission {mission_name} missing NumberOfEnemyUnits."
                        )
                    if "behavior" not in mission.enemy_units.keys():
                        report.errors.append(
                            f"ERROR: Mission {mission_name} missing CombatBehavior."
                        )
                    if "important" not in mission.enemy_units.keys():
                        report.errors.append(
                            f"ERROR: Mission {mission_name} missing EnemyUnitMissionCritical."
                        )
                    if "classes" not in mission.enemy_units.keys():
                        report.errors.append(
                            f"ERROR: Mission {mission_name} missing EnemyShipClasses."
                        )
                continue
            if not (
                (count == behavior)
                and (importance == classes)
                and (count == importance)
            ):
                report.errors.append(
                    f"ERROR: Mission {mission_name} has vessel array mismatch:"
                    + f"\n    Count: {count}"
                    + f"\n    Behaviors: {behavior}"
                    + f"\n    Criticality: {importance}"
                    + f"\n    Vessels: {classes}"
                )
    return report
