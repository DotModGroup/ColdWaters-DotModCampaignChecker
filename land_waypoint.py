"""This file holds the SeaWaypoint class, which stores one SeaWaypoint from the waypoints_sea file.

Classes:
    LandWaypoint
"""


class LandWaypoint:
    """This class stores the data for one LandWaypoint

    Attributes:
        name: str | The game-name of this waypoint
        alighnment: str | The default Alignment of this waypoint
        connected_to_waypoints: list[str] | The list of land waypoints this one is connected to
        invaded_by: list[str] | The list of "invaded by" types
    """

    def __init__(
        self,
        name: str,
        alignment: str,
        connected_to_waypoints: list[str],
        invaded_by: list[str],
    ):
        self.name = name
        self.alignment = alignment
        self.connected_to_waypoints = connected_to_waypoints
        self.invaded_by = invaded_by
