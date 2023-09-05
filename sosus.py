"""This file contains the SOSUS class, which individually stores the data for one SOSUS line
    
Classes:
    SOSUS
"""


class SOSUS:
    """This class stores the data for one SOSUS line as read in from campaign_data.

    Attributes:
        name: str = "" | Stores the game-name of this SOSUS line
        alignment: str = "" | Stores the alignment for this SOSUS line
        detection_range: int | Stores the detection range of this SOSUS line
        start_location: tuple[float, float] = (0, 0) | Stores the start location for this SOSUS
        end_location: tuple[float, float] = (0, 0) | Stores the end location for this SOSUS
        angle: int = 0 | Stores the angle between the map locations, for game calculations

    Methods:
        None
    """

    def __init__(self):
        self.name: str = ""
        self.alignment: str = ""
        self.detection_range: int
        self.start_location: tuple[float, float] = (0, 0)
        self.end_location: tuple[float, float] = (0, 0)
        self.angle: int = 0
