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
    """Quick test for the existence of campaign_data

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()
    if not current_campaign.campaign_data.parsed:
        report.announcements.append(
            "ANNOUNCEMENT: campaign_data.txt could not be found. Many checks will be skipped."
        )
    return report
