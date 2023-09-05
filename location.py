"""This file contains the Location class,
which individually stores the data for one campaign location
    
Classes:
    Location
"""


class Location:
    """This class stores the data for one Location as read in from campaign_data.

    Attributes:
        alignment: str = "" | Stores the initial allignment for this Location
        default_aircraft: list[str] = [] | Stores the aircraft for the default alignment
        functions: list[str] = [] | Stores the list of Functions this base takes
        id: int | Stores the numerical ID of this location
        invaded_aircraft: list[str] = [] | Stores the aircraft for the invaded alignment
        land_waypoints: list[str] | Stores the IDs of all linked land waypoints
        map_position: tuple(float, float) = (0, 0) | Stores the location this
                                                     Location takes on the map
        mission_types: list[str] = [] | Stores the list of all Mission Types this
                                        base can act as a start/end for
        related_sosus: list[str] = [] | Stores any connected SOSUS lines
        sea_waypoints: list[str] = [] | Stores the IDs of all linked sea waypoints

    Methods:
        None
    """

    def __init__(self):
        self.alignment: str = ""
        self.default_aircraft: list[str] = []
        self.functions: list[str] = []
        self.location_id: int
        self.invaded_aircraft: list[str] = []
        self.land_waypoints: list[str]
        self.map_position: tuple[float, float] = (0, 0)
        self.mission_types: list[str] = []
        self.related_sosus: list[str] = []
        self.sea_waypoints: list[str] = []
