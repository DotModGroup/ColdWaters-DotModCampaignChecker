"""This module contains the class for storing the parsed vessel inventory

Classes:
    VesselInventory
"""


class VesselInventory:
    """This class stores a vessel inventory and the selectors for a campaign

    Attributes:
        vessel_inventory: dict[str, int] = {} | Stores a list of vessels and their counts
            vesselname: count | The number of vessels of class vessel_name
        selectors: dict[str, list[str]] = {} | Stores all selectors and all vessels in each selector
            selectorname: listofvessels | Store vessels associated with a selector

    Methods:
        None
    """

    def __init__(self, campaign_directory: str):
        self.vessel_inventory: dict[str, int] = {}
        self.selectors: dict[str, list[str]] = {}
        try:
            with open(
                f"{campaign_directory}\\vessel_selector.txt", mode="r", encoding="utf-8"
            ) as vessel_inventory:
                reading_selectors = False
                for line in vessel_inventory:
                    if line.startswith("[Selectors]"):
                        reading_selectors = True
                        continue
                    if not reading_selectors:
                        try:
                            self.vessel_inventory[line[:-1].split("=")[0]] = int(
                                line[:-1].split("=")[1]
                            )
                        except IndexError:
                            continue
                    if reading_selectors:
                        try:
                            self.selectors[line[:-1].split("=")[0]] = (
                                line[:-1].split("=")[1].split(",")
                            )
                        except IndexError:
                            continue
        except FileNotFoundError:
            pass
