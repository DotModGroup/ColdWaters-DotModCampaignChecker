def location_parser(campaign_directory: str):
    with open(
        f"{campaign_directory}\\campaign_data.txt", mode="r", encoding="utf-8"
    ) as campaign_data:
        for line in campaign_data:
            if line.startswith("Alignment="):
                pass
