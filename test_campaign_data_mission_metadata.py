from campaign import Campaign
from report import Report


def test_campaign_data_mission_metadata(current_campaign: Campaign) -> Report:
    report = Report()
    if not (
        (len(current_campaign.campaign_data.player_mission_data["types"]) - 2)
        == len(current_campaign.campaign_data.player_mission_data["frequencies"])
        == len(current_campaign.campaign_data.player_mission_data["thresholds"])
        == len(current_campaign.campaign_data.player_mission_data["counts"])
    ):
        report.errors.append(
            "ERROR: Mismatch in Player Mission Metadata:"
            + f"\nTypes: {len(current_campaign.campaign_data.player_mission_data['types'])}"
            + f"\nFrequencies: {len(current_campaign.campaign_data.player_mission_data['frequencies'])}"
            + f"\nThresholds: {len(current_campaign.campaign_data.player_mission_data['thresholds'])}"
            + f"\nCounts: {len(current_campaign.campaign_data.player_mission_data['counts'])}"
        )
    if (
        abs(
            total := sum(
                [
                    float(x)
                    for x in current_campaign.campaign_data.player_mission_data[
                        "frequencies"
                    ]
                ]
            )
            - 1
        )
        > 0.00001
    ):
        report.errors.append(
            f"ERROR: Player Mission Frequencies sum to {total + 1:.5f} and not 1."
        )

    if (
        abs(
            total := sum(
                [
                    float(x)
                    for x in current_campaign.campaign_data.ai_mission_data[
                        "frequencies"
                    ]
                ]
            )
            - 1
        )
        > 0.00001
    ):
        report.errors.append(
            f"ERROR: AI Mission Frequencies sum to {total + 1:.5f} and not 1."
        )
    return report
