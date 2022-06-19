import os
from report import Report


def write_report(report_list: list[Report]):
    with open(
        f"{os.path.dirname(os.path.abspath(__file__))}\\reports.txt",
        mode="w",
        encoding="utf-8",
    ) as file:
        # Write top-priority announcments to the top
        file.write("ANNOUNCEMENTS:\n")
        for report in report_list:
            for announcement in report.announcements:
                file.write(f"{announcement}\n")

        file.write("\n")

        # Write each report in a separate
        file.write("REPORTS:\n")
        for report in report_list:
            for header in report.header:
                file.write(f"{header}\n")
            file.write("\n")
            for error in report.errors:
                file.write(f"{error}\n")
            file.write("\n")
            for warning in report.warnings:
                file.write(f"{warning}\n")
            file.write("\n")
            for info in report.infos:
                file.write(f"{info}\n")
