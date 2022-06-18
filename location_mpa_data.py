class MPA_Data:
    def __init__(
        self,
        aircraft_type: str,
        aircraft_type_invaded: str,
        prep_time: int,
        search_between: tuple[int, int],
        search_distance: int,
    ):
        self.aircraft_type = aircraft_type
        self.aircraft_type_invaded = aircraft_type_invaded
        self.prep_time = prep_time
        self.search_between = search_between
        self.search_distance = search_distance
