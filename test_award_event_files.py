"""This file contains a test for event files for the award events found in awards.txt.

Imports From:
    campaign.py
    report.py

Functions:
    test_award_event_files()
"""
from campaign import Campaign
from report import Report


def test_award_event_files(current_campaign: Campaign):
    """Test each award to ensure the relevant events exist

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    for award in current_campaign.awards.patrol_awards:
        if award not in current_campaign.language_info.events.events:
            report.errors.append(f"ERROR: Patrol Award {award} missing event file.")

    for award in current_campaign.awards.cumulative_awards:
        if award not in current_campaign.language_info.events.events:
            report.errors.append(f"ERROR: Cumulative Award {award} missing event file.")

    for award in current_campaign.awards.wounded_awards:
        if award not in current_campaign.language_info.events.events:
            report.errors.append(f"ERROR: Wounded Award {award} missing event file.")

    return report
