import os


class Events:
    def __init__(self, campaign_directory: str, current_language: str):
        event_file_directory = (
            f"{campaign_directory}\\language_{current_language}\\events"
        )
        self.events: list[str] = []
        for event_file in os.listdir(event_file_directory):
            if (
                event_file == "_notes.txt"
                or os.path.isfile(f"{event_file_directory}\\{event_file}") is False
            ):
                continue
            self.events.append(event_file[:-4])
        for content_file in f"{event_file_directory}\\content":
            self.events.append(content_file[:-4])
