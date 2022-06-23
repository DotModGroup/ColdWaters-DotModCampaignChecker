"""This file contains tests to ensure all required regular and special events exist

Imports From:
    campaign.py
    report.py

Functions:
    test_campaign_data_events()
"""
from campaign import Campaign
from report import Report


def test_campaign_data_events(current_campaign: Campaign) -> Report:
    """Test all events specified for completeness and existance in the filesystem

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()
    important_special_events = [
        "START",
        "ENEMY_INVASION_SEA",
        "ENEMY_INVASION_LAND",
        "ENEMY_INVASION_AIR",
        "PLAYER_LIBERATION_SEA",
        "PLAYER_LIBERATION_LAND",
        "PLAYER_LIBERATION_AIR",
        "ARMISTICE_ADVANTAGE",
        "ARMISTICE_DISADVANTAGE",
        "WIN",
        "DRAW",
        "FAIL",
        "CRITICAL_FAIL",
        "COURT_MARTIAL",
        "RESCUE",
        "CAPTURE",
        "LOST_AT_SEA",
        "STATISTICS",
    ]

    for event in current_campaign.campaign_data.events:
        if event not in current_campaign.events.events:
            report.errors.append(
                f"ERROR: Event {event} found in campaign_data but not present in language files!"
            )

    for special_event in current_campaign.campaign_data.special_events.keys():
        if special_event in important_special_events:
            important_special_events.remove(special_event)

    if len(important_special_events) > 0:
        report.errors.append(
            f"ERROR: The following important events are not found in campaign_data:"
            f"\n    {important_special_events}"
        )
    return report
