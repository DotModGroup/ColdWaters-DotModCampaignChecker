from campaign import Campaign
from report import Report


def test_mission_events(current_campaign: Campaign):
    report = Report()

    for mission in current_campaign.missions:
        try:
            if (win := mission.events["win"]) not in current_campaign.events.events:
                report.errors.append(
                    f'ERROR: Mission {mission.name} calls for missing win event "{win}".'
                )
        except KeyError:
            continue

        try:
            if (fail := mission.events["fail"]) not in current_campaign.events.events:
                report.errors.append(
                    f'ERROR: Mission {mission.name} calls for missing fail event "{fail}".'
                )
        except KeyError:
            continue

    return report
