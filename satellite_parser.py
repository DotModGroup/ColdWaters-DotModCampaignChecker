"""This file contains the code used to parse all the aircraft
in campaign_data and give it back to the campaign_data object

Imports From:
    satellite.py

Functions:
    satellite_parser()
"""
from satellite import Satellite


def satellite_parser(campaign_directory: str) -> list[Satellite]:
    """Generate a list of Satellites given a read campaign data file

    Parameters:
        campaign_directory: str | A filepath to a campaign data file containing Satellites

    Returns:
        list[Satellite] | A list of parsed Satellite
    """
    aircraft_list: list[Satellite] = []
    reading_satellites = False
    # Done to appease MyPy
    current_satellite: Satellite = Satellite()
    try:
        with open(
            f"{campaign_directory}\\campaign_data.txt", mode="r", encoding="utf-8"
        ) as campaign_data:
            for line in campaign_data:
                if line.strip() == "[Satellites]":
                    reading_satellites = True
                    continue
                if not reading_satellites:
                    continue
                if line.strip() == "[Locations]":
                    reading_satellites = False
                    if current_satellite.name != "":
                        aircraft_list.append(current_satellite)
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

    except FileNotFoundError:
        return []
