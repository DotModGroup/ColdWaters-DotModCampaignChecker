from campaign import Campaign
from report import Report


def test_campaign_data_mission_integrity(current_campaign: Campaign) -> Report:
    report = Report()

    for mission_file in current_campaign.missions:
        if (
            mission_file.name not in current_campaign.campaign_data.player_missions
            and mission_file.name not in current_campaign.campaign_data.ai_missions
            and "LOCATION" not in mission_file.name
        ):
            report.infos.append(
                f"INFO: Mission {mission_file.name} is not in "
                "campaign_data mission lists and so cannot appear."
            )

    for mission in (
        current_campaign.campaign_data.player_missions
        + current_campaign.campaign_data.ai_missions
    ):
        for current_mission in current_campaign.missions:
            if current_mission.name == mission:
                break
        else:
            report.errors.append(
                f"ERROR: Mission {mission} does not have a corresponding mission file."
            )

    return report
