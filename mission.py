"""This file contains the Mission class, which individually stores the data for one Mission

Classes:
    Mission
"""


class Mission:
    """This class stores a singular mission as loaded from a mission file

    Attributes:
        name: str | The name of the mission
        vessel_restrictions: dict[str, list[str] | str] = {} | A dict of vessel restrictions
            onlyfor: vesseltypes | Only vessels of these types can get this mission
            notfor: vesseltypes | Vessels of these types cannot get this mission
            maxcost: number | Vessels with >= than this cost cannot get this mission
            mincost: number | Vessels with <= than this cost cannot get this mission
        start_location: dict[str, str | list[str]] = {} | The starting alignment and function
            function: functions | Mission will start from a location with one of these functions
            alignment: alignment | Mission will only start from a place with this alignment
        end_location: dict[str, str | list[str]] = {} | The ending alignment and function
            function: functions | Mission will end at a location with one of these functions
            alignment: alignment | Mission will only end at a place with this alignment
        enemy_units: dict[str, list[str]] = {} | The enemy units generated for this mission
            count: rangeofcounts | The number of units generated from this group
            behavior: behavior | Determines if units in this group will act agressivly or not
            important: boolean | Determines if vessels from this group must be sunk for success
            classes: shipclasses | The list of vessels and selectors this group will choose from
        events: dict[str, str] = {} | The win and loss events
            win: event | Event to be played when the mission is won
            fail: event | Event to be played when the mission is failed
        waypoints: dict[str, list[str]] = {}
            mustuse: waypoints | This group must go to every one of these waypoints
            softuse: waypoints | This group must go to at least one of these waypoints
            notallowed: waypoints | This group may not pass through any of these waypoints

    Methods:
        None
    """

    # Note that this class includes its own parser
    def __init__(self, filename: str):
        self.name = filename.split("\\")[-1][:-4]
        self.vessel_restrictions: dict[str, list[str] | str] = {}
        self.start_location: dict[str, str | list[str]] = {}
        self.end_location: dict[str, str | list[str]] = {}
        self.enemy_units: dict[str, list[str]] = {}
        self.events: dict[str, str] = {}
        self.waypoints: dict[str, list[str]] = {}

        for line in open(filename, mode="r", encoding="utf-8"):
            if line.startswith("MissionType="):
                self.type = line[:-1].split("=")[1]

            if line.startswith("AllowedOnlyFor="):
                self.vessel_restrictions["onlyfor"] = line[:-1].split("=")[1].split(",")

            if line.startswith("ForbiddenFor="):
                self.vessel_restrictions["notfor"] = line[:-1].split("=")[1].split(",")

            if line.startswith("AllowedOnlyForCostBelow="):
                self.vessel_restrictions["maxcost"] = line[:-1].split("=")[1]

            if line.startswith("AllowedOnlyForCostHigherThan="):
                self.vessel_restrictions["mincost"] = line[:-1].split("=")[1]

            if line.startswith("StartLocation="):
                self.start_location["function"] = line[:-1].split("=")[1].split(",")

            if line.startswith("StartAlignment="):
                self.start_location["alignment"] = line[:-1].split("=")[1]

            if line.startswith("EndLocation="):
                self.end_location["function"] = line[:-1].split("=")[1].split(",")

            if line.startswith("EndAlignment="):
                self.end_location["alignment"] = line[:-1].split("=")[1]

            if line.startswith("MustUseWaypoints"):
                self.waypoints["mustuse"] = line[:-1].split("=")[1].split(",")

            if line.startswith("UseAtLeastOneWaypointOf="):
                self.waypoints["softuse"] = line[:-1].split("=")[1].split(",")

            if line.startswith("ProhibitedWaypoints="):
                self.waypoints["notallowed"] = line[:-1].split("=")[1].split(",")

            if line.startswith("NumberOfEnemyUnits="):
                self.enemy_units["count"] = line[:-1].split("=")[1].split(",")

            if line.startswith("CombatBehaviour="):
                self.enemy_units["behavior"] = line[:-1].split("=")[1].split(",")

            if line.startswith("EnemyUnitMissionCritical="):
                self.enemy_units["important"] = line[:-1].split("=")[1].split(",")

            if line.startswith("EnemyShipClasses"):
                self.enemy_units["classes"] = (
                    line.removesuffix("\n").split("=")[1].split(",")
                )

            if line.startswith("EventWin="):
                self.events["win"] = line[:-1].split("=")[1]

            if line.startswith("EventFail="):
                self.events["fail"] = line.split("=")[1].removesuffix("\n")
