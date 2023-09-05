"""This file contains tests for the various airbases found in the campaign_data locations

Imports From:
    campaign.py
    report.py

Functions:
    test_campaign_data_airbase_aircraft_types()
"""
from campaign import Campaign
from report import Report


def test_campaign_data_airbase_aircraft_types(current_campaign: Campaign) -> Report:
    """Test all airbases in campaign_data to check their aircraft are valid

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    for location in current_campaign.campaign_data.locations:
        if "AIRBASE" in location.functions:
            if location.default_aircraft == []:
                report.errors.append(
                    f"ERROR: Location ID {location.location_id} is registered as "
                    "AIRBASE but has no AircraftType."
                )
            else:
                for aircraft in location.default_aircraft:
                    if aircraft not in (
                        campaign_aircraft.name
                        for campaign_aircraft in current_campaign.campaign_data.aircraft
                    ):
                        report.errors.append(
                            f"ERROR: Location ID {location.location_id} has "
                            f"unrecognized AircraftType {aircraft}."
                        )
            if location.invaded_aircraft == []:
                report.errors.append(
                    f"ERROR: Location ID {location.location_id} is registered as "
                    "AIRBASE but has no AircraftTypeInvaded."
                )
            else:
                for aircraft in location.invaded_aircraft:
                    if aircraft not in (
                        campaign_aircraft.name
                        for campaign_aircraft in current_campaign.campaign_data.aircraft
                    ):
                        report.errors.append(
                            f"ERROR: Location ID {location.location_id} has unrecognized "
                            f"AircraftTypeInvaded {aircraft}."
                        )
        else:
            if location.default_aircraft != []:
                report.infos.append(
                    f"INFO: Location ID {location.location_id} is not registered as "
                    "AIRBASE but has defined AircraftType."
                )
            if location.invaded_aircraft != []:
                report.infos.append(
                    f"INFO: Location ID {location.location_id} is not registered as "
                    "AIRBASE but has defined AircraftTypeInvaded."
                )

    return report
