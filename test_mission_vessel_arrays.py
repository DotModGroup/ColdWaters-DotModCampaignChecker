from campaign import Campaign
from report import Report


def test_mission_vessel_arrays(current_campaign: Campaign) -> Report:
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
