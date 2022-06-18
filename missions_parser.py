import os
from mission import Mission


def mission_parser(campaign_directory: str) -> list[Mission]:
    missions_list: list[Mission] = []
    mission_directory = f"{campaign_directory}\\missions"
    for file in os.listdir(mission_directory):
        if os.path.isfile(f"{mission_directory}\\{file}"):
            missions_list.append(Mission(f"{mission_directory}\\{file}"))
    return missions_list
