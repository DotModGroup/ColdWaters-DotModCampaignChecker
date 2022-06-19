from mission import Mission
from campaign_data import CampaignData
from vessel_inventory import VesselInventory


class Campaign:
    def __init__(
        self,
        missions: list[Mission],
        campaign_data: CampaignData,
        vessel_inventory: VesselInventory,
    ):
        self.missions = missions
        self.campaign_data = campaign_data
        self.vessel_inventory = vessel_inventory
