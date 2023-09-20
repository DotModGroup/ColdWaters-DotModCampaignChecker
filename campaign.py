"""This file contains tests to ensure all required regular and special events exist

Imports From:
    awards.py
    campaign_data.py
    language_info.py
    mission.py
    summary.py
    vessel_inventory.py

Classes:
    Campaign
"""
from awards import Awards
from mission import Mission
from campaign_data import CampaignData
from vessel_inventory import VesselInventory
from language_info import LangaugeInfo
from summary import Summary
from waypoints import Waypoints


class Campaign:
    """This class describes a fully parsed campaign, with missions and all other data

    Attributes:
        missions: list[Mission] | This is the list of all Missions in this Campaign
        campaign_data: CampaignData | This stores all of the info parsed from campaign_data.txt
        vessel_inventory: VesselInventory | This stores the parsed vessel inventories and selectors
        awards: Awards | This stores all Awards in the Campaign
        summary: Summary | This stores the campaign's parsed Summary file
        waypoints: Waypoints | This stores all of the campaign's land and sea waypoints

    Methods:
        None
    """

    def __init__(
        self,
        awards: Awards,
        missions: list[Mission],
        campaign_data: CampaignData,
        vessel_inventory: VesselInventory,
        language_info: LangaugeInfo,
        summary: Summary,
        waypoints: Waypoints,
    ):
        self.awards = awards
        self.missions = missions
        self.campaign_data = campaign_data
        self.vessel_inventory = vessel_inventory
        self.language_info = language_info
        self.summary = summary
        self.waypoints = waypoints
