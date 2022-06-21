class CampaignData:
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
                    if len(split := line[:-1].split("=")) == 3:
                        self.special_events[split[2]] = split[1]
                    self.events.append(line[:-1].split("=")[1])
