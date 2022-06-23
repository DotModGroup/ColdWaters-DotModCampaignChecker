"""This file has the campaign_parser, which is a macro for parsing an entire campaign

Imports From:
    campaign.py
    campaign_data.py
    language_info.py
    mission.py
    missions_parser.py
    vessel_inventory.py

Functions:
    campaign_parser()
"""
from campaign import Campaign
from campaign_data import CampaignData
from mission import Mission
from missions_parser import mission_parser
from vessel_inventory import VesselInventory
from language_info import LangaugeInfo

# This file will run each parser and collect the data
# Data is returned as one monolitic Campaign object
def campaign_parser(campaign_directory: str, current_language: str) -> Campaign:
    """Parse the individual parts of a campaign and return a completed campaign object

    Parameters:
        campaign_directory: str | A filepath to the campaign to be parsed
        current_language: str | A two-letter language code for the language files to check

    Returns:
        Campaign | Campaign object made with the parsed data
    """
    mission_list: list[Mission] = mission_parser(campaign_directory)
    campaign_data: CampaignData = CampaignData(campaign_directory)
    vessel_inventory: VesselInventory = VesselInventory(campaign_directory)
    language_info: LangaugeInfo = LangaugeInfo(campaign_directory, current_language)
    return Campaign(mission_list, campaign_data, vessel_inventory, language_info)
