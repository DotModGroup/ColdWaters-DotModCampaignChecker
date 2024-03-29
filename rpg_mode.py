"""This file contains the RPGMode class, which contains a read-in rpg_mode.txt.

Classes:
    RPGMode
"""


class RPGMode:
    """This class stores the data for the rpg_mode.txt file.

    Attributes:
        xp_for_next_level: list[int] | The list of exprience required for every level-up
        xo_names: list[str] | The list of all possible XO names.

    Methods:
        None
    """

    def __init__(self, rpg_mode_file: str) -> None:
        self.main_text = False
        self.xp_for_next_level: list[int] = []
        self.xo_names: list[str] = []
        self.xp_message: str = ""
        self.level_up_message: str = ""
        self.crew_levels: list[str] = []
        self.crew_level_messages: list[str] = []

        with open(rpg_mode_file, encoding="utf-8") as rpg_file:
            for line in rpg_file:
                if line.startswith("[MAIN TEXT]"):
                    self.main_text = True

                if line.startswith("ExpForNextLevel="):
                    self.xp_for_next_level = [
                        int(xp) for xp in line.strip().split("=")[1].split(",")
                    ]

                if line.startswith("XO_Variants="):
                    self.xo_names = line.removesuffix("\n").split("=")[1].split(",")

                if line.startswith("ExpForMission="):
                    self.xp_message = line.removesuffix("\n").split("=")[1]

                if line.startswith("NewLevelGained="):
                    self.level_up_message = line.removesuffix("\n").split("=")[1]

                if line.startswith("CrewQualities="):
                    self.crew_levels = line.strip().split("=")[1].split(",")

                if line.startswith("CrewQualitiesDescription="):
                    self.crew_level_messages = (
                        line.removesuffix("\n").split("=")[1].split("|")
                    )
