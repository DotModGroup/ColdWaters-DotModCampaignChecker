import os
from report import Report
from campaigns_parser import campaign_parser
from write_reports import write_report

# ----------------Test Modules Here----------------------------
from test_mission_vessel_arrays import test_mission_vessel_arrays
from test_mission_vessel_counts import test_mission_vessel_counts

# ----------------End Test Modules-----------------------------

# Current plan: This file will simply be an if name == main: main() block
# main() will first parse a specified whole campaign with the campaign_parser
# then it will run each check and collect the report data
# and then write the report to a file


def main():
    campaign_number = int(input("Select campaign number to check: "))
    campaign_directory = f"{os.path.dirname(os.path.abspath(__file__))}\\campaign\\campaign{campaign_number:03}"
    all_reports: list[Report] = []

    current_campaign = campaign_parser(campaign_directory)

    all_reports.append(test_mission_vessel_arrays(current_campaign))
    all_reports.append(test_mission_vessel_counts(current_campaign))

    write_report(all_reports)

    print("Program completed.")


if __name__ == "__main__":
    main()
