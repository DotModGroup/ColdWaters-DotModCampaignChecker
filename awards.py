"""This file holds the Awards class, which holds all of the awards at once.

Classes:
    Awards
"""


class Awards:
    """This class stores all events from a single campaign

    Attributes:
        patrol_awards: list[str] = [] | List of patrol awards as pulled from awards.txt
        cumulative_awards: list[str] = [] | List of cumulative awards as pulled from awards.txt
        wounded_awards: list[str] = [] | List of wounded awards as pulled from awards.txt


    Methods:
        None
    """

    def __init__(self, campaign_directory: str) -> None:
        self.patrol_awards: list[str] = []
        self.cumulative_awards: list[str] = []
        self.wounded_awards: list[str] = []

        awards_file = campaign_directory + "\\awards.txt"
        for line in open(awards_file, mode="r", encoding="utf-8"):
            if line.startswith("PatrolAwards="):
                self.patrol_awards = line[:-1].split("=")[1].split(",")
            if line.startswith("CumulativeAwards="):
                self.cumulative_awards = line[:-1].split("=")[1].split(",")
            if line.startswith("WoundedAwards="):
                self.wounded_awards = line[:-1].split("=")[1].split(",")
