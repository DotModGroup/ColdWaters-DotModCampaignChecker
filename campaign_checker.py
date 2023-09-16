"""This module is the top-level file to run for the Campaign Checker

Imports From:
    os
    campaigns_parser.py
    report.py
    test_award_event_files.py
    test_campaign_data_events.py
    test_campaign_data_airbase_aircraft_types.py
    test_campaign_data_mission_integrity.py
    test_campaign_data_mission_metadata.py
    test_campaign_data_mission_types.py
    test_campaign_data_sosus_lines.py
    test_campaign_data_special_mission_types
    test_campaign_mission_index.py
    test_campaign_mission_types.py
    test_mission_vessel_arrays.py
    test_mission_vessel_counts.py
    test_mission_vessel_inventory_integrity.py
    test_mission_events.py
    test_mission_language_files.py
    write_reports.py

Functions:
    main()
"""

import os
from campaigns_parser import campaign_parser
from report import Report
from write_reports import write_report

# ----------------Test Modules Here----------------------------
from test_award_event_files import test_award_event_files
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
from test_mission_language_files import test_mission_language_files
from test_campaign_mission_index import test_campaign_mission_index
from test_campaign_data_mission_types import test_campaign_data_mission_types
from test_campaign_data_special_mission_types import (
    test_campaign_data_special_mission_types,
)

from test_campaign_data_airbase_aircraft_types import (
    test_campaign_data_airbase_aircraft_types,
)
from test_campaign_data_sosus_lines import test_campaign_data_sosus_lines
from test_campaign_rpg_mode import test_campaign_rpg_mode

# ----------------End Test Modules-----------------------------

# Current plan: This file will simply be an if name == main: main() block
# main() will first parse a specified whole campaign with the campaign_parser
# then it will run each check and collect the report data
# and then write the report to a file


def main():
    """Take a campaign number, parse campaign data, and run a series of tests on the parsed data

    Parameters:
        None

    Returns:
        None
    """
    campaign_number = int(input("Select campaign number to check: "))
    current_language = input("Input two character language code: ")
    campaign_directory = f"{os.getcwd()}" + f"\\campaign\\campaign{campaign_number:03}"
    all_reports: list[Report] = []

    current_campaign = campaign_parser(campaign_directory, current_language)

    all_reports.append(test_award_event_files(current_campaign))
    all_reports.append(test_campaign_data_mission_metadata(current_campaign))
    all_reports.append(test_campaign_data_mission_integrity(current_campaign))
    all_reports.append(test_campaign_mission_types(current_campaign))
    all_reports.append(test_campaign_mission_index(current_campaign))
    all_reports.append(test_campaign_data_events(current_campaign))
    all_reports.append(test_mission_vessel_arrays(current_campaign))
    all_reports.append(test_mission_vessel_counts(current_campaign))
    all_reports.append(test_mission_vessel_inventory_integrity(current_campaign))
    all_reports.append(test_mission_events(current_campaign))
    all_reports.append(test_mission_language_files(current_campaign))
    all_reports.append(test_campaign_data_mission_types(current_campaign))
    all_reports.append(test_campaign_data_special_mission_types(current_campaign))
    all_reports.append(test_campaign_data_airbase_aircraft_types(current_campaign))
    all_reports.append(test_campaign_data_sosus_lines(current_campaign))
    all_reports.append(test_campaign_rpg_mode(current_campaign))

    write_report(all_reports)

    print("Program completed.")


if __name__ == "__main__":
    main()
