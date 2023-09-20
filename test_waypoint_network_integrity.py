"""This file contains tests to ensure the waypoint network is somewhat sane

Imports From:
    campaign.py
    report.py

Functions:
    test_waypoint_network_integrity()
"""
from campaign import Campaign
from report import Report


def test_waypoint_network_integrity(current_campaign: Campaign):
    """Test the waypoint network for sanity

    Parameters:
        current_campaign: Campaign | The parsed campaign to be tested

    Returns:
        Report | The completed Report to be returned
    """
    report = Report()

    # Check that all land connects are defined on both ends
    # yes this is awful code running O(N^4) but /shrug
    if current_campaign.waypoints.land_waypoints is not None:
        for land_waypoint in current_campaign.waypoints.land_waypoints:
            for connected_waypoint in land_waypoint.connected_to_waypoints:
                if connected_waypoint not in [
                    waypoint.name
                    for waypoint in current_campaign.waypoints.land_waypoints
                ]:
                    report.errors.append(
                        f"ERROR: Land Waypoint {land_waypoint.name} has non-existant waypoint "
                        f"{connected_waypoint} as a ConnectedZone."
                    )
                else:
                    connected_to_waypoint_temp = [
                        waypoint if waypoint.name == connected_waypoint else None
                        for waypoint in current_campaign.waypoints.land_waypoints
                    ]
                    connected_to_waypoint = []
                    for possible_connected_waypoint in connected_to_waypoint_temp:
                        if possible_connected_waypoint is not None:
                            connected_to_waypoint.append(possible_connected_waypoint)
                    if len(connected_to_waypoint) > 1:
                        report.errors.append(
                            f"ERROR: More than one land waypoint with name {connected_waypoint}."
                        )
                    else:
                        if (
                            land_waypoint.name
                            not in connected_to_waypoint[0].connected_to_waypoints
                        ):
                            report.warnings.append(
                                f"WARNING: Land waypoint {land_waypoint.name} lists waypoint "
                                f"{connected_to_waypoint[0].name} as connected but not vice-versa."
                            )
    else:
        report.errors.append("ERROR: waypoints_region.txt not found.")

    if current_campaign.waypoints.sea_waypoints is not None:
        for sea_waypoint in current_campaign.waypoints.sea_waypoints:
            for north_waypoint in sea_waypoint.north_waypoints:
                if north_waypoint not in [
                    potential_north_waypoint.name
                    for potential_north_waypoint in current_campaign.waypoints.sea_waypoints
                ]:
                    report.errors.append(
                        f"ERROR: Waypoint {sea_waypoint.name} has non-existent waypoint "
                        f"{north_waypoint} as a North Waypoint."
                    )

                for (
                    potential_north_waypoint
                ) in current_campaign.waypoints.sea_waypoints:
                    if potential_north_waypoint.name == north_waypoint:
                        if (
                            sea_waypoint.name
                            not in potential_north_waypoint.south_waypoints
                        ):
                            report.warnings.append(
                                f"WARNING: Waypoint {sea_waypoint.name} has waypoint "
                                f"{north_waypoint} as a North Waypoint but "
                                f"{north_waypoint} does not have {sea_waypoint.name} "
                                "as a South Waypoint."
                            )

            for south_waypoint in sea_waypoint.south_waypoints:
                if south_waypoint not in [
                    potential_south_waypoint.name
                    for potential_south_waypoint in current_campaign.waypoints.sea_waypoints
                ]:
                    report.errors.append(
                        f"ERROR: Waypoint {sea_waypoint.name} has non-existent waypoint "
                        f"{south_waypoint} as a South Waypoint."
                    )

                for (
                    potential_south_waypoint
                ) in current_campaign.waypoints.sea_waypoints:
                    if potential_south_waypoint.name == south_waypoint:
                        if (
                            sea_waypoint.name
                            not in potential_south_waypoint.north_waypoints
                        ):
                            report.warnings.append(
                                f"WARNING: Waypoint {sea_waypoint.name} has waypoint "
                                f"{south_waypoint} as a South Waypoint but "
                                f"{south_waypoint} does not have {sea_waypoint.name} "
                                "as a North Waypoint."
                            )

            for east_waypoint in sea_waypoint.east_waypoints:
                if east_waypoint not in [
                    potential_east_waypoint.name
                    for potential_east_waypoint in current_campaign.waypoints.sea_waypoints
                ]:
                    report.errors.append(
                        f"ERROR: Waypoint {sea_waypoint.name} has non-existent waypoint "
                        f"{east_waypoint} as an East Waypoint."
                    )

                for potential_east_waypoint in current_campaign.waypoints.sea_waypoints:
                    if potential_east_waypoint.name == east_waypoint:
                        if (
                            sea_waypoint.name
                            not in potential_east_waypoint.west_waypoints
                        ):
                            report.warnings.append(
                                f"WARNING: Waypoint {sea_waypoint.name} has waypoint "
                                f"{east_waypoint} as an East Waypoint but "
                                f"{east_waypoint} does not have {sea_waypoint.name} "
                                "as a West Waypoint."
                            )

            for west_waypoint in sea_waypoint.west_waypoints:
                if west_waypoint not in [
                    potential_west_waypoint.name
                    for potential_west_waypoint in current_campaign.waypoints.sea_waypoints
                ]:
                    report.errors.append(
                        f"ERROR: Waypoint {sea_waypoint.name} has non-existent waypoint "
                        f"{west_waypoint} as a West Waypoint."
                    )

                for potential_west_waypoint in current_campaign.waypoints.sea_waypoints:
                    if potential_west_waypoint.name == west_waypoint:
                        if (
                            sea_waypoint.name
                            not in potential_west_waypoint.east_waypoints
                        ):
                            report.warnings.append(
                                f"WARNING: Waypoint {sea_waypoint.name} has waypoint "
                                f"{west_waypoint} as a West Waypoint but "
                                f"{west_waypoint} does not have {sea_waypoint.name} "
                                "as an East Waypoint."
                            )

    return report
