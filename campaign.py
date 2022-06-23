"""This file contains tests to ensure all required regular and special events exist

Imports From:
    campaign_data.py
    mission.py
    events.py
    vessel_inventory.py

Classes:
    Campaign
"""
from mission import Mission
from campaign_data import CampaignData
from vessel_inventory import VesselInventory
from events import Events


class Campaign:
    """This class describes a fully parsed campaign, with missions and all other data

    Attributes:
        missions: list[Mission] | This is the list of all Missions in this Campaign
        campaign_data: CampaignData | This stores all of the info parsed from campaign_data.txt
        vessel_inventory: VesselInventory | This stores the parsed vessel inventories and selectors
        events: Events | This stores all events in this Campaign

    Methods:
        None
    """

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
