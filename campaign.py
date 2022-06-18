from mission import Mission
from campaign_data import CampaignData


class Campaign:
    def __init__(self, missions: list[Mission], campaign_data: CampaignData):
        self.missions = missions
        self.campaign_data = campaign_data
