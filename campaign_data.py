"""This file contains the CampaignData class which handles and parses the data in campaign_data.txt

Imports From:
    aircraft.py
    aircraft_parser.py
    location.py
    locations_parser.py
    sosus.py
    sosus_parser.py

Classes:
    Mission
"""

from aircraft import Aircraft
from aircraft_parser import aircraft_parser
from location import Location
from locations_parser import locations_parser
from satellite import Satellite
from satellite_parser import satellite_parser
from sosus import SOSUS
from sosus_parser import sosus_parser


class CampaignData:
    """This class contains the data parsed from the current campaign's campaign_data.txt

    Attributes:
        events: list[str] = [] | Stores the events parsed from the file
        special_events: dict[str, str] = {} | Stores special event types and associated events
            specialeventtype: eventname | Markes eventname as of special type specialeventtype
        player_missions: list[str] = [] | Lists all player missions found in the list
        ai_missions: list[str] = [] | Lists all AI missions found in the list
        player_mission_data: dict[str, list[str]] = {} | Stores metadata about player missions
            types: listofmissiontypes | Stores all mission types parsed
            frequencies: listoffrequencies | Stores all of the frequency values, as str
            thresholds: listofthresholds | Stores all minimum point threshold values
            counts: listofcounts | Stores all counts for missions, as str
        ai_mission_data: dict[str, list[str]] = {}
            types: listofaimissiontypes | Stores all AI mission types
            frequencies: listofaimissionfrequencies | Stores the frequency list for AI missions

    Methods:
        None
    """

    def __init__(self, campaign_directory: str):
        self.locations: list[Location] = locations_parser(campaign_directory)
        self.sosus_lines: list[SOSUS] = sosus_parser(campaign_directory)
        self.aircraft: list[Aircraft] = aircraft_parser(campaign_directory)
        self.satellites: list[Satellite] = satellite_parser(campaign_directory)

        try:
            with open(
                f"{campaign_directory}\\campaign_data.txt", mode="r", encoding="utf-8"
            ) as campaign_data:
                self.events: list[str] = []
                self.special_events: dict[str, str] = {}
                self.ai_missions: list[str] = []
                self.player_missions: list[str] = []
                self.ai_mission_data: dict[str, list[str]] = {}
                self.player_mission_data: dict[str, list[str]] = {}
                self.player_first_missions: list[str] = []
                self.player_default_missions: list[str] = []
                self.player_failsafe_mission: str = ""

                for line in campaign_data:
                    if line.startswith("PlayerMissionTypes"):
                        self.player_mission_data["types"] = (
                            line.strip().split("=")[1].split(",")
                        )

                    if line.startswith("PlayerMissionFrequency"):
                        self.player_mission_data["frequencies"] = (
                            line.strip().split("=")[1].split(",")
                        )

                    if line.startswith("PlayerMissionThreshold"):
                        self.player_mission_data["thresholds"] = (
                            line.strip().split("=")[1].split(",")
                        )

                    if line.startswith("PlayerMissionCount"):
                        self.player_mission_data["counts"] = (
                            line.strip().split("=")[1].split(",")
                        )

                    if line.startswith("FirstMissionTypes"):
                        self.player_first_missions = (
                            line.strip().split("=")[1].split(",")
                        )

                    if line.startswith("DefaultMissionTypes"):
                        self.player_default_missions = (
                            line.strip().split("=")[1].split(",")
                        )

                    if line.startswith("FailsafeMissionType"):
                        self.player_failsafe_mission = line.strip().split("=")[1]

                    if line.startswith("Non-PlayerMissionTypes"):
                        self.ai_mission_data["types"] = (
                            line.strip().split("=")[1].split(",")
                        )

                    if line.startswith("Non-PlayerMissionFrequency"):
                        self.ai_mission_data["frequencies"] = (
                            line.strip().split("=")[1].split(",")
                        )

                    if line.startswith("Mission="):
                        self.player_missions.append(line.strip().split("=")[1])

                    if line.startswith("Non-PlayerMission="):
                        self.ai_missions.append(line.strip().split("=")[1])

                    if line.startswith("Event="):
                        if len(split := line.strip().split("=")) == 3:
                            self.special_events[split[2]] = split[1]
                        self.events.append(line.strip().split("=")[1])

                self.parsed = True
        except FileNotFoundError:
            self.parsed = False
