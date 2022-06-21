from campaign import Campaign
from report import Report


def test_campaign_mission_types(current_campaign: Campaign) -> Report:
    report = Report()
    for mission in current_campaign.missions:
        try:
            if (
                mission.type
                not in current_campaign.campaign_data.player_mission_data["types"]
                and mission.type
                not in current_campaign.campaign_data.ai_mission_data["types"]
            ):
                report.errors.append(
                    f"ERROR: Mission {mission.name} of unrecognized type {mission.type}."
                )
        except AttributeError:
            continue

    for mission in current_campaign.missions:
        try:
            part_name = mission.name.split("_")[0]
            for part in mission.name.split("_")[1:-1]:
                part_name += f"_{part}"
            if mission.type != part_name and mission.type != mission.name:
                report.errors.append(
                    f"Mission {mission.name} is not of the same type as specified in the file!"
                )
        except AttributeError:
            continue
    return report
