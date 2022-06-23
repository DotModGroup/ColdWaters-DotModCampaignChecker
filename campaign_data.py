"""This file contains the CampaignData class which handles and parses the data in campaign_data.txt

Classes:
    Mission
"""


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
        with open(
            f"{campaign_directory}\\campaign_data.txt", mode="r", encoding="utf-8"
        ) as campaign_data:
            self.events: list[str] = []
            self.special_events: dict[str, str] = {}
            self.ai_missions: list[str] = []
            self.player_missions: list[str] = []
            self.ai_mission_data: dict[str, list[str]] = {}
            self.player_mission_data: dict[str, list[str]] = {}
            for line in campaign_data:
                if line.startswith("PlayerMissionTypes="):
                    self.player_mission_data["types"] = (
                        line[:-1].split("=")[1].split(",")
                    )

                if line.startswith("PlayerMissionFrequency="):
                    self.player_mission_data["frequencies"] = (
                        line[:-1].split("=")[1].split(",")
                    )

                if line.startswith("PlayerMissionThreshold="):
                    self.player_mission_data["thresholds"] = (
                        line[:-1].split("=")[1].split(",")
                    )

                if line.startswith("PlayerMissionCount="):
                    self.player_mission_data["counts"] = (
                        line[:-1].split("=")[1].split(",")
                    )

                if line.startswith("Non-PlayerMissionTypes="):
                    self.ai_mission_data["types"] = line[:-1].split("=")[1].split(",")

                if line.startswith("Non-PlayerMissionFrequency="):
                    self.ai_mission_data["frequencies"] = (
                        line[:-1].split("=")[1].split(",")
                    )

                if line.startswith("Mission="):
                    self.player_missions.append(line[:-1].split("=")[1])

                if line.startswith("Non-PlayerMission="):
                    self.ai_missions.append(line[:-1].split("=")[1])

                if line.startswith("Event="):
                    if len(split := line.removesuffix("\n").split("=")) == 3:
                        self.special_events[split[2]] = split[1]
                    self.events.append(line.removesuffix("\n").split("=")[1])
