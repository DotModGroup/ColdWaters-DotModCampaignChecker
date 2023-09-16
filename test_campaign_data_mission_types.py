"""This file contains tests for the names of mission types 

Imports From:
    campaign.py
    report.py

Functions:
    test_campaign_data_mission_types()
"""
from campaign import Campaign
from report import Report


def test_campaign_data_mission_types(current_campaign: Campaign) -> Report:
    """Test each mission type to ensure that it contains no invalid characters

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    if not current_campaign.campaign_data.parsed:
        return report

    for mission_type in current_campaign.campaign_data.player_mission_data["types"]:
        if any(char.isdigit() for char in mission_type):
            report.warnings.append(
                f"WARNING: Mission type {mission_type} has invalid name."
            )
    for mission_type in current_campaign.campaign_data.ai_mission_data["types"]:
        if any(char.isdigit() for char in mission_type):
            report.warnings.append(
                f"WARNING: Mission type {mission_type} has invalid name."
            )
    return report
