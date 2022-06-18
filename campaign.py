from mission import Mission
from campaign_meta_data import Campaign_Meta_Data


class Campaign:
    def __init__(
        self,
        meta_data: Campaign_Meta_Data,
        missions: list[Mission],
        events: list[str],
        locations: list[locations],
        waypoints: list[]
    ):
        self.meta_data = meta_data
        self.missions = missions
        self.events = events
        self.locations = locations
