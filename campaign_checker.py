import os
from report import Report
from campaigns_parser import campaign_parser
from write_reports import write_report

# ----------------Test Modules Here----------------------------
from test_campaign_data_mission_metadata import test_campaign_data_mission_metadata
from test_mission_vessel_arrays import test_mission_vessel_arrays
from test_mission_vessel_counts import test_mission_vessel_counts
from test_mission_vessel_inventory_integrity import (
    test_mission_vessel_inventory_integrity,
)
from test_campaign_data_events import test_campaign_data_events
from test_mission_events import test_mission_events
from test_campaign_mission_types import test_campaign_mission_types
from test_campaign_data_mission_integrity import test_campaign_data_mission_integrity

# ----------------End Test Modules-----------------------------

# Current plan: This file will simply be an if name == main: main() block
# main() will first parse a specified whole campaign with the campaign_parser
# then it will run each check and collect the report data
# and then write the report to a file


def main():
    CURRENT_LANGUAGE = "en"
    campaign_number = int(input("Select campaign number to check: "))
    campaign_directory = f"{os.path.dirname(os.path.abspath(__file__))}\\campaign\\campaign{campaign_number:03}"
    all_reports: list[Report] = []

    current_campaign = campaign_parser(campaign_directory, CURRENT_LANGUAGE)

    all_reports.append(test_campaign_data_mission_metadata(current_campaign))
    all_reports.append(test_campaign_data_mission_integrity(current_campaign))
    all_reports.append(test_campaign_mission_types(current_campaign))
    all_reports.append(test_campaign_data_events(current_campaign))
    all_reports.append(test_mission_vessel_arrays(current_campaign))
    all_reports.append(test_mission_vessel_counts(current_campaign))
    all_reports.append(test_mission_vessel_inventory_integrity(current_campaign))
    all_reports.append(test_mission_events(current_campaign))

    write_report(all_reports)

    print("Program completed.")


if __name__ == "__main__":
    main()
