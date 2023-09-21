"""This file contains tests to ensure all specified locations pass basic sanity checks.

Imports From:
    campaign.py
    report.py

Functions:
    test_campaign_data_locations()
"""
from campaign import Campaign
from report import Report


def test_locations_language_info(current_campaign: Campaign) -> Report:
    """Test all locations specified for sanity

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    if current_campaign.language_info.location_names is not None:
        if len(current_campaign.campaign_data.locations) != len(
            current_campaign.language_info.location_names
        ):
            report.errors.append(
                f"ERROR: There are {len(current_campaign.campaign_data.locations)} "
                "Locations specified in campaign_data.txt but "
                f"{len(current_campaign.language_info.location_names)} LocationNames "
                "in campaign_map_data.txt."
            )
    else:
        report.errors.append(
            f"ERROR: language_{current_campaign.language_info.language}\\"
            "campaign_map_data.txt not found."
        )

    if current_campaign.waypoints.sea_waypoints is not None:
        if current_campaign.language_info.sea_names is not None:
            if len(current_campaign.waypoints.sea_waypoints) != len(
                current_campaign.language_info.sea_names
            ):
                report.errors.append(
                    f"ERROR: There are {len(current_campaign.waypoints.sea_waypoints)} "
                    "sea waypoints specified in waypoints_sea.txt but "
                    f"{len(current_campaign.language_info.sea_names)} sea names "
                    "in waypoints_sea_names.txt."
                )
        else:
            report.errors.append(
                f"ERROR: language_{current_campaign.language_info.language}\\"
                "waypoints_sea_names.txt not found."
            )

    if current_campaign.waypoints.land_waypoints is not None:
        if current_campaign.language_info.region_names is not None:
            if len(current_campaign.waypoints.land_waypoints) != len(
                current_campaign.language_info.region_names
            ):
                report.errors.append(
                    f"ERROR: There are {len(current_campaign.waypoints.land_waypoints)} "
                    "land waypoints specified in waypoints_region.txt but "
                    f"{len(current_campaign.language_info.region_names)} region names "
                    "in waypoints_region_names.txt."
                )
        else:
            report.errors.append(
                f"ERROR: language_{current_campaign.language_info.language}\\"
                "waypoints_region_names.txt not found."
            )

    return report
