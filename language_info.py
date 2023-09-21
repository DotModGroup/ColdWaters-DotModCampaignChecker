"""This file holds all data relevant to the parsed language files
    
Imports From:
    events.py
    mission_language_files.py
    
Classes:
    LanguageInfo
"""
import os

from events import Events
from mission_language_files import MissionLanguageFiles


class LangaugeInfo:
    """This class stores all mission language files found for the specified language

    Attributes:
        language: str | The two-letter code for the current language
        events: list[str] = [] | List of all events as pilled from the files
        mission_language_files: list[str] = [] | Stores the names of all parsed mission
            language files

    Methods:
        None
    """

    def __init__(self, campaign_directory: str, current_language: str):
        self.language = current_language
        self.events = Events(campaign_directory, current_language)
        self.mission_language_files = MissionLanguageFiles(
            campaign_directory, current_language
        )

        self.description_file = (
            True
            if os.path.exists(
                f"{campaign_directory}\\language_{current_language}\\description.txt"
            )
            else False
        )

        try:
            with open(
                f"{campaign_directory}\\language_{current_language}\\campaign_map_data.txt",
                encoding="utf8",
            ) as map_data:
                self.location_names: list[str] | None = [
                    line.strip().split("=")[1]
                    for line in map_data.readlines()
                    if line.startswith("LocationName=")
                ]

        except FileNotFoundError:
            self.location_names = None

        try:
            with open(
                f"{campaign_directory}\\language_{current_language}\\"
                "waypoints_region_names.txt",
                encoding="utf8",
            ) as region_names:
                self.region_names: list[str] | None = [
                    line.strip().split("=")[0]
                    for line in region_names.readlines()
                    if not line.startswith("Regions=")
                ]
        except FileNotFoundError:
            self.region_names = None

        try:
            with open(
                f"{campaign_directory}\\language_{current_language}\\"
                "waypoints_sea_names.txt",
                encoding="utf8",
            ) as sea_names:
                self.sea_names: list[str] | None = [
                    line.strip() for line in sea_names.readlines()
                ]
        except FileNotFoundError:
            self.sea_names = None
