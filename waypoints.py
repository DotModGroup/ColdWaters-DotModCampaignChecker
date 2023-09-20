"""This file stores the Waypoints class, which store information about a campaign's waypoints

Classes:
    Waypoints: Stores a campaign's waypoint data
"""

from sea_waypoint import SeaWaypoint
from land_waypoint import LandWaypoint


class Waypoints:
    """This class stores all of the waypoints in the campaign

    Attributes:
        land_waypoints: list[LandWaypoint] | A list containing all of the land waypoints
        sea_waypoints: list[SeaWaypoint] | A list containing all of the sea waypoints

    """

    def __init__(self, camapaign_directory) -> None:
        self.sea_waypoints: list[SeaWaypoint] | None = []
        self.land_waypoints: list[LandWaypoint] | None = []

        waypoint_sea_filepath = f"{camapaign_directory}\\waypoints_sea.txt"
        waypoint_land_filepath = f"{camapaign_directory}\\waypoints_region.txt"

        try:
            with open(waypoint_sea_filepath, encoding="utf8") as waypoint_sea_file:
                current_waypoint_name: str = ""
                current_waypoint_north: list[str] = []
                current_waypoint_south: list[str] = []
                current_waypoint_east: list[str] = []
                current_waypoint_west: list[str] = []

                for line in waypoint_sea_file.readlines():
                    if line.startswith("WaypointName="):
                        if current_waypoint_name:
                            self.sea_waypoints.append(
                                SeaWaypoint(
                                    current_waypoint_name,
                                    current_waypoint_north,
                                    current_waypoint_south,
                                    current_waypoint_east,
                                    current_waypoint_west,
                                )
                            )
                        current_waypoint_name = line.strip().split("=")[1]
                        current_waypoint_north = []
                        current_waypoint_south = []
                        current_waypoint_east = []
                        current_waypoint_west = []

                    if line.startswith("NorthWaypoints="):
                        current_waypoint_north = line.strip().split("=")[1].split(",")

                    if line.startswith("SouthWaypoints="):
                        current_waypoint_south = line.strip().split("=")[1].split(",")

                    if line.startswith("EastWaypoints="):
                        current_waypoint_east = line.strip().split("=")[1].split(",")

                    if line.startswith("WestWaypoints="):
                        current_waypoint_west = line.strip().split("=")[1].split(",")

            if current_waypoint_name:
                self.sea_waypoints.append(
                    SeaWaypoint(
                        current_waypoint_name,
                        current_waypoint_north,
                        current_waypoint_south,
                        current_waypoint_east,
                        current_waypoint_west,
                    )
                )

        except FileNotFoundError:
            self.sea_waypoints = None

        try:
            with open(waypoint_land_filepath, encoding="utf8") as waypoint_land_file:
                current_waypoint_name = ""
                current_waypoint_alignment: str = ""
                current_waypoint_connected_to: list[str] = []
                current_waypoint_invaded_by: list[str] = []

                for line in waypoint_land_file:
                    if line.startswith("WaypointName="):
                        if current_waypoint_name:
                            self.land_waypoints.append(
                                LandWaypoint(
                                    current_waypoint_name,
                                    current_waypoint_alignment,
                                    current_waypoint_connected_to,
                                    current_waypoint_invaded_by,
                                )
                            )
                        current_waypoint_name = line.strip().split("=")[1]
                        current_waypoint_alignment = ""
                        current_waypoint_connected_to = []
                        current_waypoint_invaded_by = []

                    if line.startswith("Alignment="):
                        current_waypoint_alignment = line.strip().split("=")[1]

                    if line.startswith("ConnectedZones="):
                        current_waypoint_connected_to = (
                            line.strip().split("=")[1].split(",")
                        )

                    if line.startswith("InvadedBy="):
                        current_waypoint_invaded_by = (
                            line.strip().split("=")[1].split(",")
                        )

                if current_waypoint_name:
                    self.land_waypoints.append(
                        LandWaypoint(
                            current_waypoint_name,
                            current_waypoint_alignment,
                            current_waypoint_connected_to,
                            current_waypoint_invaded_by,
                        )
                    )

        except FileNotFoundError:
            self.land_waypoints = None
