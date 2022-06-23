"""This file contains tests for the win/loss events found in mission files.

Imports From:
    campaign.py
    report.py

Functions:
    test_mission_events()
"""
from campaign import Campaign
from report import Report


def test_mission_events(current_campaign: Campaign):
    """Test each mission to ensure the specified win/loss events exist

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    for mission in current_campaign.missions:
        try:
            if (
                win := mission.events["win"]
            ) not in current_campaign.language_info.events.events:
                report.errors.append(
                    f'ERROR: Mission {mission.name} calls for missing win event "{win}".'
                )
        except KeyError:
            continue

        try:
            if (
                fail := mission.events["fail"]
            ) not in current_campaign.language_info.events.events:
                report.errors.append(
                    f'ERROR: Mission {mission.name} calls for missing fail event "{fail}".'
                )
        except KeyError:
            continue

    return report
