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

    if not current_campaign.campaign_data.parsed:
        return report

    important_special_events = [
        "START",
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
        if event not in current_campaign.language_info.events.events:
            report.errors.append(
                f"ERROR: Event {event} found in campaign_data but not present in language files!"
            )

    for special_event in current_campaign.campaign_data.special_events.keys():
        if special_event in important_special_events:
            important_special_events.remove(special_event)

    if len(important_special_events) > 0:
        report.warnings.append(
            f"WARNING: The following important events are not found in campaign_data:"
            f"\n    {important_special_events}"
        )

    if (
        "PLAYER_INVASION_SEA" not in important_special_events
        or "PLAYER_INVASION_LAND" not in important_special_events
        or "PLAYER_INVASION_AIR" not in important_special_events
    ):
        if "ENEMY_LIBERATION_SEA" in important_special_events:
            report.warnings.append(
                "WARNING: Player side is able to INVADE territory, "
                "but no ENEMY_LIBERATION_SEA event found."
            )

        if "ENEMY_LIBERATION_LAND" in important_special_events:
            report.warnings.append(
                "WARNING: Player side is able to INVADE territory, "
                "but no ENEMY_LIBERATION_LAND event found."
            )

        if "ENEMY_LIBERATION_AIR" in important_special_events:
            report.warnings.append(
                "WARNING: Player side is able to INVADE territory, "
                "but no ENEMY_LIBERATION_AIR event found."
            )

    if (
        "ENEMY_INVASION_SEA" not in important_special_events
        or "ENEMY_INVASION_LAND" not in important_special_events
        or "ENEMY_INVASION_AIR" not in important_special_events
    ):
        if "PLAYER_LIBERATION_SEA" in important_special_events:
            report.warnings.append(
                "WARNING: Enemy side is able to INVADE territory, "
                "but no PLAYER_LIBERATION_SEA event found."
            )

        if "PLAYER_LIBERATION_LAND" in important_special_events:
            report.warnings.append(
                "WARNING: Player side is able to INVADE territory, "
                "but no PLAYER_LIBERATION_LAND event found."
            )

        if "PLAYER_LIBERATION_AIR" in important_special_events:
            report.warnings.append(
                "WARNING: Player side is able to INVADE territory, "
                "but no PLAYER_LIBERATION_AIR event found."
            )

    if (
        "PLAYER_LIBERATION_SEA" not in important_special_events
        or "PLAYER_LIBERATION_LAND" not in important_special_events
        or "PLAYER_LIBERATION_AIR" not in important_special_events
    ):
        if "ENEMY_INVASION_SEA" in important_special_events:
            report.infos.append(
                "INFO: Player side is able to LIBERATE territory, "
                "but no ENEMY_INVASION_SEA event found."
            )

        if "ENEMY_INVASION_LAND" in important_special_events:
            report.infos.append(
                "INFO: Player side is able to LIBERATE territory, "
                "but no ENEMY_INVASION_LAND event found."
            )

        if "ENEMY_INVASION_AIR" in important_special_events:
            report.infos.append(
                "INFO: Player side is able to LIBERATE territory, "
                "but no ENEMY_INVASION_AIR event found."
            )

    if (
        "ENEMY_LIBERATION_SEA" not in important_special_events
        or "ENEMY_LIBERATION_LAND" not in important_special_events
        or "ENEMY_LIBERATION_AIR" not in important_special_events
    ):
        if "PLAYER_INVASION_SEA" in important_special_events:
            report.infos.append(
                "INFO: Enemy side is able to LIBERATE territory, "
                "but no PLAYER_INVASION_SEA event found."
            )

        if "PLAYER_INVASION_LAND" in important_special_events:
            report.infos.append(
                "INFO: Enemy side is able to LIBERATE territory, "
                "but no PLAYER_INVASION_LAND event found."
            )

        if "PLAYER_INVASION_AIR" in important_special_events:
            report.infos.append(
                "INFO: Enemy side is able to LIBERATE territory, "
                "but no PLAYER_INVASION_AIR event found."
            )

    return report
