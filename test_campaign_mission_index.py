"""This file contains tests for the mission indexes of mission files

Imports From:
    campaign.py
    report.py

Functions:
    test_campaign_mission_index()
"""
from campaign import Campaign
from report import Report


def test_campaign_mission_index(current_campaign: Campaign) -> Report:
    """Test each mission to ensure that missions for each type are all consecutively 0-indexed

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()
    mission_types: dict[str, list[int]] = {}
    for mission in current_campaign.missions:
        try:
            if mission.type not in mission_types:
                mission_types[mission.type] = []
                mission_types[mission.type].append(int(mission.name.split("_")[-1]))
        except AttributeError:
            continue

    for mission_type, missions in mission_types.items():
        missions.sort()
        num = 0
        for mission_number in missions:
            if mission_number != num:
                report.errors.append(
                    f"ERROR: Mission type {mission_type} missing mission number {num}."
                )
            num += 1
    return report
