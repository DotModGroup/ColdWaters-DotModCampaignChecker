"""This file holds the MissionLanguageFiles class, which holds all found mission language files

Imports From:
    os

Classes:
    MissionLanguageFiles
"""

import os


class MissionLanguageFiles:
    """This class stores all mission language files found for the specified language

    Attributes:
        language_files: list[str] = [] | Stores the names of all parsed language files

    Methods:
        None
    """

    def __init__(self, campaign_directory: str, current_language: str):
        mission_file_directory = (
            f"{campaign_directory}\\language_{current_language}\\missions"
        )
        self.language_files: list[str] = []
        for event_file in os.listdir(mission_file_directory):
            if os.path.isfile(f"{mission_file_directory}\\{event_file}") is False:
                continue
            self.language_files.append(event_file[:-4])
