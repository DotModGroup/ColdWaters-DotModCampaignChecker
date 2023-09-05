"""This file contains the Aircraft class,
which individually stores the data for one campaign aircraft type
    
Classes:
    Aircraft
"""


class Satellite:
    """This class stores the data for one Aircraft type as read in from campaign_data.

    Attributes:
        name: str = "" | Stores this Satellite's name
        faction: str = "" | Stores the faction (i.e. draw color) for this Satellite
        satellite_speed: int = 0 | Stores this Satellite's Speed
        detection_range: int = 0 | Stores this Satellite's Detection Range

    Methods:
        None
    """

    def __init__(self):
        self.name: str = ""
        self.faction: str = ""
        self.satellite_speed: int = 0
        self.detection_range: int = 0
