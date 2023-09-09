"""This file contains the code used to parse all the locations
in campaign_data and give it back to the campaign_data object

Imports From:
    sosus.py

Functions:
    sosus_parser()
"""

from sosus import SOSUS


def sosus_parser(campaign_directory: str) -> list[SOSUS]:
    """Generate a list of Locations given a read campaign data file

    Parameters:
        campaign_directory: str | A filepath to a campaign data file containing Locations

    Returns:
        list[Locations] | A list of parsed Locations
    """
    with open(
        f"{campaign_directory}\\campaign_data.txt", mode="r", encoding="utf-8"
    ) as campaign_data:
        sosus_list: list[SOSUS] = []
        reading_sosus = False
        # Done to appease MyPy
        current_sosus: SOSUS = SOSUS()

        for line in campaign_data:
            if line.strip() == "[SOSUS]":
                reading_sosus = True
                continue
            if not reading_sosus:
                continue
            if line.strip() == "[PLAYER MISSIONS]":
                reading_sosus = False
                if current_sosus.name != "":
                    sosus_list.append(current_sosus)
                continue

            if line.strip().startswith("SOSUSName"):
                if current_sosus.name != "":
                    sosus_list.append(current_sosus)
                current_sosus = SOSUS()
                current_sosus.name = line.strip().split("=")[1]

            if line.strip().startswith("SOSUSStartPosition"):
                current_sosus.start_location = (
                    float(line.split("=")[1].split(",")[0]),
                    float(line.split("=")[1].split(",")[1]),
                )

            if line.strip().startswith("SOSUSEndPosition"):
                current_sosus.end_location = (
                    float(line.split("=")[1].split(",")[0]),
                    float(line.split("=")[1].split(",")[1]),
                )

            if line.strip().startswith("SOSUSAngle"):
                current_sosus.angle = int(line.strip().split("=")[1])

            if line.strip().startswith("SOSUSDetectionRange"):
                current_sosus.detection_range = int(line.strip().split("=")[1])

            if line.strip().startswith("SOSUSAlignment"):
                current_sosus.alignment = line.strip().split("=")[1]

        return sosus_list
