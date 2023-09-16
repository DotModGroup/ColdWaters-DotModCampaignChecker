"""This file writes a list of reports to a text file.

Imports From:
    campaign.py
    report.py

Functions:
    write_report()
"""
import os
from report import Report


def write_report(report_list: list[Report]):
    """Write a list of Reports to disk in a human-readable format

    Parameters:
        report_list: list[Report] | A list of reports to write to disk

    Returns:
        None
    """
    with open(
        f"{os.getcwd()}\\reports.txt",
        mode="w",
        encoding="utf-8",
    ) as file:
        final_report: Report = Report()
        for report in report_list:
            for announcement in report.announcements:
                final_report.announcements.append(announcement)
            for error in report.errors:
                final_report.errors.append(error)
            for warning in report.warnings:
                final_report.warnings.append(warning)
            for info in report.infos:
                final_report.infos.append(info)

        # Write top-priority announcments to the top
        file.write("ANNOUNCEMENTS:\n")
        for announcement in final_report.announcements:
            file.write(f"{announcement}\n")
        file.write("\n")

        # Write each level separately
        file.write("REPORTS:\n")
        for error in final_report.errors:
            file.write(f"{error}\n")
        if final_report.errors:
            file.write("\n")

        for warning in final_report.warnings:
            file.write(f"{warning}\n")
        if final_report.warnings:
            file.write("\n")

        for info in final_report.infos:
            file.write(f"{info}\n")
