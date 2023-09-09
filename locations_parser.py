"""This file contains the code used to parse all the locations
in campaign_data and give it back to the campaign_data object

Imports From:
    location.py

Functions:
    locations_parser()
"""

from location import Location


def locations_parser(campaign_directory: str) -> list[Location]:
    """Generate a list of Locations given a read campaign data file

    Parameters:
        campaign_directory: str | A filepath to a campaign data file containing Locations

    Returns:
        list[Locations] | A list of parsed Locations
    """
    with open(
        f"{campaign_directory}\\campaign_data.txt", mode="r", encoding="utf-8"
    ) as campaign_data:
        locations: list[Location] = []
        current_location_id = -2
        # Done to appease MyPy
        current_location: Location = Location()

        for line in campaign_data:
            if line.strip() == "[Locations]":
                current_location_id = -1
                continue
            if current_location_id == -2:
                continue
            if line.strip() == "[SOSUS]" or line.strip() == "[PLAYER MISSIONS]":
                current_location_id = -2
                if current_location_id != -1:
                    locations.append(current_location)
                continue

            if line.strip().startswith("Alignment"):
                if current_location_id != -1:
                    locations.append(current_location)
                current_location = Location()
                current_location_id += 1
                current_location.location_id = current_location_id
                current_location.alignment = line.strip().split("=")[1]

            if line.strip().startswith("BaseMapPosition"):
                current_location.map_position = (
                    float(line.split("=")[1].split(",")[0]),
                    float(line.split("=")[1].split(",")[1]),
                )

            if line.strip().startswith("Function"):
                current_location.functions = line.strip().split("=")[1].split(",")

            if line.strip().startswith("RelatedSOSUS"):
                current_location.related_sosus = line.strip().split("=")[1].split(",")

            if line.strip().startswith("AircraftType"):
                current_location.default_aircraft = (
                    line.strip().split("=")[1].split(",")
                )

            if line.strip().startswith("AircraftTypeInvaded"):
                current_location.invaded_aircraft = (
                    line.strip().split("=")[1].split(",")
                )

            if line.strip().startswith("MissionTypes"):
                current_location.mission_types = line.strip().split("=")[1].split(",")

            if line.strip().startswith("LinksToWaypoint"):
                current_location.sea_waypoints = line.strip().split("=")[1].split(",")

            if line.strip().startswith("LinksToReigonWaypoint"):
                current_location.land_waypoints = line.strip().split("=")[1].split(",")

        return locations
