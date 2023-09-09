"""This file contains tests for the SOSUS lines found in campaign_data 

Imports From:
    math
    typing
    
    campaign.py
    report.py
    sosus.py

Functions:
    angle_check()
    test_campaign_data_sosus_lines()
"""
import math
from typing import Optional

from campaign import Campaign
from report import Report
from sosus import SOSUS


def test_campaign_data_sosus_lines(current_campaign: Campaign) -> Report:
    """Test all airbases in campaign_data to check their aircraft are valid

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    for sosus_line in current_campaign.campaign_data.sosus_lines:
        # if angle_report := angle_check(sosus_line):
        #    report.warnings.append(angle_report)

        if sosus_line.detection_range != 120:
            report.infos.append(
                f"INFO: Detection range of SOSUS Line {sosus_line.name} differs from "
                "default of 120. This may cause visual inconsistencies with detection."
            )

    return report


def angle_check(sosus_line: SOSUS) -> Optional[str]:
    """Calculates the angle between the two points of a SOSUS line.
        Seemingly not what the game is looking for with "ANGLE"

    Parameters:
        sosus_line: SOSUS | The current SOSUS line to examine

    Returns:
        Optional[str] | None if there is no problem, otherwise a report about the angle
    """
    calculated_sosus_angle = (
        math.acos(
            (
                (sosus_line.start_location[0] * sosus_line.end_location[0])
                + (sosus_line.start_location[1] * sosus_line.end_location[1])
            )
            / (
                math.sqrt(
                    sosus_line.start_location[0] ** 2
                    + sosus_line.start_location[1] ** 2
                )
                * math.sqrt(
                    sosus_line.end_location[0] ** 2 + sosus_line.end_location[1] ** 2
                )
            )
        )
        * 180
        / math.pi
    )
    if abs(abs(sosus_line.angle) - abs(round(calculated_sosus_angle))) > 1:
        return (
            f"WARNING: Calculated absolute value of angle of {abs(calculated_sosus_angle)} "
            f"degrees for SOSUS Line {sosus_line.name} differs from absolute value of "
            f"specified angle of {abs(sosus_line.angle)} by a considerable margin."
        )
    return None
