# ColdWaters-DotModCampaignChecker
This project is designed to automatically check a DotMod campaign for issues to find bugs before campaigns even go live.
This is a "static checker" (like MyPy for Python) and is designed to be run cold on any campaign.

## Current Checks:
- All vessel arrays in campaign missions are the same length. 
- Maximum and minimum vessles in missions, as well as critical vessels. 
- Player and AI mission metadata, including frequency sums. 
- Vessels provided in mission files exist in vessel_inventory

## Changelog
- v0.01: First three checks
- v0.02: Added vessel name integrity check