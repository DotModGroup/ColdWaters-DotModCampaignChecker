class Mission:

    # Note that this class includes its own parser
    def __init__(self, filename: str):
        self.name = filename.split("\\")[-1][:-4]
        self.vessel_restrictions: dict[str, list[str] | str] = {}
        self.start_location: dict[str, str | list[str]] = {}
        self.end_location: dict[str, str | list[str]] = {}
        self.enemy_units: dict[str, list[str]] = {}
        self.events: dict[str, str] = {}

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
                self.end_location["alignment"] = line[:-1].split("=")[1].split(",")

            if line.startswith("EndAlignment="):
                self.end_location["alignment"] = line[:-1].split("=")[1]

            if line.startswith("MustUseWaypoints"):
                self.must_use_waypoints = line[:-1].split("=")[1].split(",")

            if line.startswith("UseAtLeastOneWaypointOf="):
                self.soft_use_waypoints = line[:-1].split("=")[1].split(",")

            if line.startswith("ProhibitedWaypoints="):
                self.prohibited_waypoints = line[:-1].split("=")[1].split(",")

            if line.startswith("NumberOfEnemyUnits="):
                self.enemy_units["count"] = line[:-1].split("=")[1].split(",")

            if line.startswith("CombatBehaviour="):
                self.enemy_units["behavior"] = line[:-1].split("=")[1].split(",")

            if line.startswith("EnemyUnitMissionCritical="):
                self.enemy_units["important"] = line[:-1].split("=")[1].split(",")

            if line.startswith("EnemyShipClasses"):
                self.enemy_units["classes"] = line[:-1].split("=")[1].split(",")

            if line.startswith("EventWin="):
                self.events["win"] = line[:-1].split("=")[1]

            if line.startswith("EventFail="):
                self.events["win"] = line[:-1].split("=")[1]
