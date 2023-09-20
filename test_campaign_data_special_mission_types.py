"""This file contains tests for the names of mission types 

Imports From:
    campaign.py
    report.py

Functions:
    test_campaign_data_special_mission_types()
"""
from campaign import Campaign
from report import Report


def test_campaign_data_special_mission_types(current_campaign: Campaign) -> Report:
    """Test the special mission types to ensure they are present and valid

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    if current_campaign.campaign_data.parsed:
        # Check for existence of default mission type
        if current_campaign.campaign_data.player_default_missions == []:
            report.errors.append("ERROR: No default missions specified.")

        # Check for existence of failsafe mission type
        if current_campaign.campaign_data.player_failsafe_mission == "":
            report.warnings.append("WARNING: No failsafe mission specified.")

        # Verify sanity of first, default, and failsafe mission types
        for mission_type in current_campaign.campaign_data.player_first_missions:
            if (
                mission_type
                not in current_campaign.campaign_data.player_mission_data["types"]
            ):
                report.errors.append(
                    f"ERROR: First mission type {mission_type} is an unrecognized mission type."
                )

        for mission_type in current_campaign.campaign_data.player_default_missions:
            if (
                mission_type
                not in current_campaign.campaign_data.player_mission_data["types"]
            ):
                report.errors.append(
                    f"ERROR: Default mission type {mission_type} is an unrecognized mission type."
                )

        if (
            current_campaign.campaign_data.player_failsafe_mission
            not in current_campaign.campaign_data.player_mission_data["types"]
            and current_campaign.campaign_data.player_failsafe_mission
        ):
            report.errors.append(
                "ERROR: Failsafe mission type "
                f"{current_campaign.campaign_data.player_failsafe_mission} is an "
                "unrecognized mission type."
            )

    return report
