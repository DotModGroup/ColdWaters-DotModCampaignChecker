"""This file holds the SeaWaypoint class, which stores one SeaWaypoint from the waypoints_sea file.

Classes:
    SeaWaypoint
"""


class SeaWaypoint:
    """This class stores the data for one SeaWaypoint

    Attributes:
        name: str | The game-name of this waypoint
        north_waypoints: list[str] | The list of waypoints to the North of this one
        south_waypoints: list[str] | The list of waypoints to the South of this one
        east_waypoints: list[str] | The list of waypoints to the East of this one
        west_waypoints: list[str] | The list of waypoints to the West of this one
    """

    def __init__(
        self,
        name: str,
        north_waypoints: list[str],
        south_waypoints: list[str],
        east_waypoints: list[str],
        west_waypoints: list[str],
    ):
        self.name = name
        self.north_waypoints = north_waypoints
        self.south_waypoints = south_waypoints
        self.east_waypoints = east_waypoints
        self.west_waypoints = west_waypoints
