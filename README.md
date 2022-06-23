# ColdWaters-DotModCampaignChecker
This project is designed to automatically check a DotMod campaign for issues to find bugs before campaigns even go live.
This is a "static checker" (like MyPy for Python) and is designed to be run cold on any campaign.

## Current Checks:
- All vessel arrays in campaign missions are the same length
- Maximum and minimum vessles in missions, as well as critical vessels
- Player and AI mission metadata, including frequency sums
- Vessels provided in mission files exist in vessel_inventory
- All events provided for in campaign_data and in mission files exist
- All critical events (such as campaign loss and start events) exist
- All missions' names match the type of mission said mission is
- All missions match a type specified in campaign_data
- All missions specified in campaign_data have a file
- All missions in the campaign are specified in campaign_data

## Changelog
- v0.01: First three checks
- v0.02: Added vessel name integrity check
- v0.03: Added several new checks and fixed a few bugs for non-DotMod campaigns
- v0.04: Added documentation, and made some reports clearer