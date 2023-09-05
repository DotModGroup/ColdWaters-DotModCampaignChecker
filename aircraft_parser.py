"""This file contains the code used to parse all the aircraft
in campaign_data and give it back to the campaign_data object

Imports From:
    io

Functions:
    aircraft_parser()
"""
import io

from aircraft import Aircraft


def aircraft_parser(camapaign_data_file: io.TextIOWrapper) -> list[Aircraft]:
    """Generate a list of Aircraft given a read campaign data file

    Parameters:
        campaign_data_file: io.TextIOWrapper | A read campaign data file containing Aircraft

    Returns:
        list[Aircraft] | A list of parsed Aircraft
    """
    aircraft_list: list[Aircraft] = []
    reading_aircraft = False
    # Done to appease MyPy
    current_aircraft: Aircraft = Aircraft()

    for line in camapaign_data_file.readlines():
        if line.strip() == "[Aircraft]":
            reading_aircraft = True
            continue
        if not reading_aircraft:
            continue
        if line.strip() == "[Satellites]":
            reading_aircraft = False
            continue

        if line.strip().startswith("AircraftName"):
            if current_aircraft.name != "":
                aircraft_list.append(current_aircraft)
            current_aircraft = Aircraft()
            current_aircraft.name = line.strip().split("=")[1]

        if line.strip().startswith("AircraftFaction"):
            current_aircraft.faction = line.strip().split("=")[1]

        if line.strip().startswith("AircraftPatrolSpeed"):
            current_aircraft.patrol_speed = int(line.strip().split("=")[1])

        if line.strip().startswith("AircraftPatrolRange"):
            current_aircraft.patrol_range = int(line.strip().split("=")[1])

        if line.strip().startswith("AircraftDetectionRange"):
            current_aircraft.detection_range = int(line.strip().split("=")[1])

    return aircraft_list
