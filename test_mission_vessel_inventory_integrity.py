from campaign import Campaign
from report import Report


def test_mission_vessel_inventory_integrity(current_campaign: Campaign) -> Report:
    report = Report()

    for mission in current_campaign.missions:
        mission_name = mission.name
        all_vessels = []
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
                                and len(vessel_role.split("|")) == 0
                            ):
                                report.warnings.append(
                                    "WARNING: In mission {mission_name} critical vessel {vessel} "
                                    "has no units availible."
                                    "\n    This will prevent this mission from occuring."
                                )
        except KeyError:
            continue
        for vessel in all_vessels:
            if (
                vessel not in current_campaign.vessel_inventory.vessel_inventory.keys()
                and vessel not in current_campaign.vessel_inventory.selectors.keys()
            ):
                report.warnings.append(
                    f"WARNING: Mission {mission_name} has vessel {vessel}, "
                    "which is neither in the vessel inventory nor a valid selector!"
                )
    return report
