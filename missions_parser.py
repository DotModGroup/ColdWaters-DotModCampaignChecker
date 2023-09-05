"""This file contains the code used to parse the 
whole mission directory and give it back to a campaign

Imports From:
    os
    mission.py

Functions:
    mission_parser()
"""
import os
from mission import Mission


def mission_parser(campaign_directory: str) -> list[Mission]:
    """Generate a list of Missions given a campaign directory

    Parameters:
        campaign_directory: str | A directory pointing to the root campaign_0XX folder

    Returns:
        list[Mission] | A list of parsed Missions
    """
    missions_list: list[Mission] = []
    mission_directory = f"{campaign_directory}\\missions"
    for file in os.listdir(mission_directory):
        if os.path.isfile(f"{mission_directory}\\{file}"):
            missions_list.append(Mission(f"{mission_directory}\\{file}"))
    return missions_list
