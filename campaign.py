from mission import Mission
from campaign_data import CampaignData
from vessel_inventory import VesselInventory
from events import Events


class Campaign:
    def __init__(
        self,
        missions: list[Mission],
        campaign_data: CampaignData,
        vessel_inventory: VesselInventory,
        events: Events,
    ):
        self.missions = missions
        self.campaign_data = campaign_data
        self.vessel_inventory = vessel_inventory
        self.events = events
