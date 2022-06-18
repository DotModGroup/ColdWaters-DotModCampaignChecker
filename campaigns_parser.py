from campaign import Campaign
from mission import Mission
from missions_parser import mission_parser

# This file will run each parser and collect the data
# Data is returned as one monolitic Campaign object
def campaign_parser(campaign_directory: str) -> Campaign:
    mission_list: list[Mission] = mission_parser(campaign_directory)
    return Campaign(mission_list)
