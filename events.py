"""This file holds the Events class, which holds all of the events at once.

Imports From:
    os
    union
    
    rpg_mode.py

Classes:
    Events
"""
import os
from typing import Union

from rpg_mode import RPGMode


class Events:
    """This class stores all events from a single campaign

    Attributes:
        events: dict[str, str] = [] | List of all events and NextActions as pulled from the files

    Methods:
        None
    """

    def __init__(self, campaign_directory: str, current_language: str):
        event_file_directory = (
            f"{campaign_directory}\\language_{current_language}\\events"
        )
        self.events: dict[str, Union[str, str]] = {}

        self.rpg_mode = None

        for event_file in os.listdir(event_file_directory):
            if (
                event_file == "_notes.txt"
                or os.path.isfile(f"{event_file_directory}\\{event_file}") is False
            ):
                continue
            with open(
                f"{event_file_directory}\\{event_file}", encoding="utf-8"
            ) as open_event_file:
                for line in open_event_file:
                    if line.startswith("NextAction"):
                        self.events[
                            event_file.strip().removesuffix(".txt")
                        ] = line.strip().split("=")[1]

        for content_file in os.listdir(f"{event_file_directory}\\content"):
            if (
                os.path.isfile(f"{event_file_directory}\\content\\{content_file}")
                is not False
            ):
                self.events[content_file.strip().removesuffix(".txt")] = "content"
                if content_file.strip() == "rpg_mode.txt":
                    self.rpg_mode = RPGMode(
                        f"{event_file_directory}\\content\\rpg_mode.txt"
                    )
