"""This file holds all data relevant to the parsed language files
    
Imports From:
    events.py
    mission_language_files.py
    
Classes:
    LanguageInfo
"""

from events import Events
from mission_language_files import MissionLanguageFiles


class LangaugeInfo:
    """This class stores all mission language files found for the specified language

    Attributes:
        language: str | The two-letter code for the current language
        events: list[str] = [] | List of all events as pilled from the files
        language_files: list[str] = [] | Stores the names of all parsed language files

    Methods:
        None
    """

    def __init__(self, campaign_directory: str, current_language: str):
        self.language = current_language
        self.events = Events(campaign_directory, current_language)
        self.mission_language_files = MissionLanguageFiles(
            campaign_directory, current_language
        )
