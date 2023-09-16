"""This file contains tests for the metadata for missions provided in campaign_data

Imports From:
    campaign.py
    report.py

Functions:
    test_campaign_data_mission_metadata()
"""
from campaign import Campaign
from report import Report


def test_campaign_data_mission_metadata(current_campaign: Campaign) -> Report:
    """Test the mission metadata for errors like mismatched array lenghts

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    if not current_campaign.campaign_data.parsed:
        return report

    try:
        if not (
            (len(current_campaign.campaign_data.player_mission_data["types"]) - 2)
            == len(current_campaign.campaign_data.player_mission_data["frequencies"])
            == len(current_campaign.campaign_data.player_mission_data["thresholds"])
            == len(current_campaign.campaign_data.player_mission_data["counts"])
        ):
            report.errors.append(
                "ERROR: Mismatch in Player Mission Metadata:"
                + f"\n    Types (+2): {len(current_campaign.campaign_data.player_mission_data['types'])}"
                + f"\n    Frequencies: {len(current_campaign.campaign_data.player_mission_data['frequencies'])}"
                + f"\n    Thresholds: {len(current_campaign.campaign_data.player_mission_data['thresholds'])}"
                + f"\n    Counts: {len(current_campaign.campaign_data.player_mission_data['counts'])}"
            )
    except KeyError:
        if not (
            (len(current_campaign.campaign_data.player_mission_data["types"]) - 2)
            == len(current_campaign.campaign_data.player_mission_data["frequencies"])
            == len(current_campaign.campaign_data.player_mission_data["thresholds"])
        ):
            report.errors.append(
                "ERROR: Mismatch in Player Mission Metadata:"
                + f"\nTypes (+2): {len(current_campaign.campaign_data.player_mission_data['types'])}"
                + f"\nFrequencies: {len(current_campaign.campaign_data.player_mission_data['frequencies'])}"
                + f"\nThresholds: {len(current_campaign.campaign_data.player_mission_data['thresholds'])}"
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
