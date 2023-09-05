"""This file contains the Aircraft class,
which individually stores the data for one campaign aircraft type
    
Classes:
    Aircraft
"""


class Aircraft:
    """This class stores the data for one Aircraft type as read in from campaign_data.

    Attributes:
        name: str = "" | Stores this Aircraft's game-name
        faction: str = "" | Stores the faction (i.e. draw color) for this Aircraft
        patrol_speed: int = 0 | Stores this Aircraft's Patrol Speed
        patrol_range: int = 0 | Stores this Aircraft's Patrol Range
        detection_range: int = 0 | Stores this Aircraft's Detection Range

    Methods:
        None
    """

    def __init__(self):
        self.name: str = ""
        self.faction: str = ""
        self.patrol_speed: int = 0
        self.patrol_range: int = 0
        self.detection_range: int = 0
