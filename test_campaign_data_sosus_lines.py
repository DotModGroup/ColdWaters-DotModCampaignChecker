"""This file contains tests for the SOSUS lines found in campaign_data 

Imports From:
    math
    
    campaign.py
    report.py

Functions:
    test_campaign_data_sosus_lines()
"""
import math

from campaign import Campaign
from report import Report


def test_campaign_data_sosus_lines(current_campaign: Campaign) -> Report:
    """Test all airbases in campaign_data to check their aircraft are valid

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    for sosus_line in current_campaign.campaign_data.sosus_lines:
        calculated_sosus_angle = (
            math.acos(
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
            * 180
            / math.pi
        )
        if abs(abs(sosus_line.angle) - abs(round(calculated_sosus_angle))) > 1:
            report.warnings.append(
                f"WARNING: Calculated absolute value of angle of {abs(calculated_sosus_angle)} "
                f"degrees for SOSUS Line {sosus_line.name} differs from absolute value of "
                f"specified angle of {abs(sosus_line.angle)} by a considerable margin."
            )

        if sosus_line.detection_range != 120:
            report.infos.append(
                f"INFO: Detection range of SOSUS Line {sosus_line.name} differs from "
                "default of 120. This may cause visual inconsistencies with detection."
            )

    return report
