"""This file contains tests for the language files associated with missions

Imports From:
    campaign.py
    report.py

Functions:
    test_mission_language_files()
"""
from campaign import Campaign
from report import Report


def test_mission_language_files(current_campaign: Campaign) -> Report:
    """Test each mission to ensure that it has an associated language file

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """

    report = Report()
    if current_campaign.campaign_data.parsed:
        for player_mission in current_campaign.campaign_data.player_missions:
            if (
                player_mission
                not in current_campaign.language_info.mission_language_files.language_files
            ):
                report.errors.append(
                    f"ERROR: Mission {player_mission} lacks a language file."
                )

        for (
            language_file
        ) in current_campaign.language_info.mission_language_files.language_files:
            for mission in current_campaign.missions:
                if language_file == mission.name:
                    break
            else:
                report.infos.append(
                    f"INFO: Language file {language_file}.txt has no mission."
                )

    return report
