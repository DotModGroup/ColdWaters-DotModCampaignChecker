"""This file contains a test for the existence and sanity of rpg_mode.txt.

Imports From:
    campaign.py
    report.py

Functions:
    test_campaign_data_events()
"""
from campaign import Campaign
from report import Report


def test_campaign_rpg_mode(current_campaign: Campaign) -> Report:
    """Test the campaign's RPG Mode file for sanity.

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    rpg_mode = None

    if current_campaign.language_info.events.rpg_mode is not None:
        rpg_mode = current_campaign.language_info.events.rpg_mode

        if not current_campaign.summary.rpg_mode:
            report.infos.append(
                "INFO: rpg_mode.txt is specified but RPG Mode is disabled "
                "in summary.txt."
            )

        if not rpg_mode.xo_names:
            report.errors.append("ERORR: No XO names specified in rpg_mde.txt.")

        if len(rpg_mode.xp_for_next_level) % 4 != 0:
            report.infos.append(
                "INFO: RPG Mode crew cannot all reach max level because number "
                "of xp levels is not a multiple of 4."
            )

        if len(rpg_mode.crew_levels) != len(rpg_mode.crew_level_messages):
            report.errors.append(
                "ERROR: RPG Mode crew qualites do not all have a valid description."
            )

        if not rpg_mode.xp_message:
            report.errors.append("ERROR: No ExpForMission message specified.")

        if not rpg_mode.level_up_message:
            report.errors.append("ERROR: No NewLevelGained message specified.")

    elif current_campaign.summary.rpg_mode:
        report.errors.append(
            f"ERROR: RPG Mode enabled in summary.txt "
            f"but language_{current_campaign.language_info.language}//events"
            "//content//rpg_mode.txt not found."
        )

    return report
