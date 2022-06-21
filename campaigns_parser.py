from campaign import Campaign
from campaign_data import CampaignData
from mission import Mission
from missions_parser import mission_parser
from vessel_inventory import VesselInventory
from events import Events

# This file will run each parser and collect the data
# Data is returned as one monolitic Campaign object
def campaign_parser(campaign_directory: str, current_language: str) -> Campaign:
    mission_list: list[Mission] = mission_parser(campaign_directory)
    campaign_data: CampaignData = CampaignData(campaign_directory)
    vessel_inventory: VesselInventory = VesselInventory(campaign_directory)
    events: Events = Events(campaign_directory, current_language)
    return Campaign(mission_list, campaign_data, vessel_inventory, events)
