"""This file contains the code used to parse all the aircraft
in campaign_data and give it back to the campaign_data object

Imports From:
    io

Functions:
    satellite_parser()
"""
import io

from satellite import Satellite


def satellite_parser(camapaign_data_file: io.TextIOWrapper) -> list[Satellite]:
    """Generate a list of Satellites given a read campaign data file

    Parameters:
        campaign_data_file: io.TextIOWrapper | A read campaign data file containing Satellite

    Returns:
        list[Satellite] | A list of parsed Satellite
    """
    aircraft_list: list[Satellite] = []
    reading_satellites = False
    # Done to appease MyPy
    current_satellite: Satellite = Satellite()

    for line in camapaign_data_file.readlines():
        if line.strip() == "[Satellites]":
            reading_satellites = True
            continue
        if not reading_satellites:
            continue
        if line.strip() == "[Locations]":
            reading_satellites = False
            continue

        if line.strip().startswith("SatelliteName"):
            if current_satellite.name != "":
                aircraft_list.append(current_satellite)
            current_satellite = Satellite()
            current_satellite.name = line.strip().split("=")[1]

        if line.strip().startswith("SatelliteFaction"):
            current_satellite.faction = line.strip().split("=")[1]

        if line.strip().startswith("SatelliteSpeed"):
            current_satellite.satellite_speed = int(line.strip().split("=")[1])

        if line.strip().startswith("SatelliteDetectionRange"):
            current_satellite.detection_range = int(line.strip().split("=")[1])

    return aircraft_list
