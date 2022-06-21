import os
from report import Report


def write_report(report_list: list[Report]):
    with open(
        f"{os.path.dirname(os.path.abspath(__file__))}\\reports.txt",
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

        # Write each level separately
        file.write("REPORTS:\n")
        for header in final_report.header:
            file.write(f"{header}\n")
        file.write("\n")
        for error in final_report.errors:
            file.write(f"{error}\n")
        file.write("\n")
        for warning in final_report.warnings:
            file.write(f"{warning}\n")
        file.write("\n")
        for info in final_report.infos:
            file.write(f"{info}\n")
        file.write("\n")
