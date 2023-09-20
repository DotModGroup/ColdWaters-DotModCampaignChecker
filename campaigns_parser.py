"""This file has the campaign_parser, which is a macro for parsing an entire campaign

Imports From:
    campaign.py
    campaign_data.py
    language_info.py
    mission.py
    missions_parser.py
    summary.py
    vessel_inventory.py

Functions:
    campaign_parser()
"""
from awards import Awards
from campaign import Campaign
from campaign_data import CampaignData
from mission import Mission
from missions_parser import mission_parser
from vessel_inventory import VesselInventory
from language_info import LangaugeInfo
from summary import Summary
from waypoints import Waypoints


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
    awards: Awards = Awards(campaign_directory)
    mission_list: list[Mission] = mission_parser(campaign_directory)
    campaign_data: CampaignData = CampaignData(campaign_directory)
    vessel_inventory: VesselInventory = VesselInventory(campaign_directory)
    language_info: LangaugeInfo = LangaugeInfo(campaign_directory, current_language)
    summary: Summary = Summary(campaign_directory)
    waypoints: Waypoints = Waypoints(campaign_directory)
    return Campaign(
        awards,
        mission_list,
        campaign_data,
        vessel_inventory,
        language_info,
        summary,
        waypoints,
    )
