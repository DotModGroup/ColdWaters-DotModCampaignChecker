class CampaignData:
    def __init__(self, campaign_directory: str):
        with open(
            f"{campaign_directory}\\campaign_data.txt", mode="r", encoding="utf-8"
        ) as campaign_data:
            self.ai_missions: list[str] = []
            self.player_missions: list[str] = []
            for line in campaign_data:
                if line.startswith("Mission="):
                    self.player_missions.append(line[:-1].split("=")[1])
                if line.startswith("Non-PlayerMission="):
                    self.ai_missions.append(line[:-1].split("=")[1])
