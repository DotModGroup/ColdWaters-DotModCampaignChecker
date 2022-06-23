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
- All missions have associated language files

## Changelog
- v0.01: First three checks
- v0.02: Added vessel name integrity check
- v0.03: Added several new checks and fixed a few bugs for non-DotMod campaigns
- v0.04: Added documentation, and made some reports clearer
- v0.05: Added a new check, refactored events and language info, and fixed whitespace in docs
- v0.06: Added .ico for release .exe, and refactored to work as a .exe 

### How to Use
1. Download the latest release from the "Releases" tab on Discord. This should be a .zip containing the .exe itself.
2. Extract the .exe from the downloaded .zip to dotmod, override, or priority, in whichever one your campaign sits.
3. Run the .exe by double-clicking on it.
4. Enter just the numeral part of the campaign's number (006 would be just 6), and then enter a two letter langauge code, such as _en or _ru.
5. Wait for the program to finish (this should never take longer than a second) and open reports.txt.
6. Perform corrections on campaign based on reports.

### How to Contribute
I'm always looking for contributors on this project! The main things I ask when contributing is that A) you document all files you commit in a style similar to the one used throughout the rest of this project (or DM me on Discord for ny little styleguide which I use for myself), and B) try to keep the code style similar to that which is presented thusfar in this project. I reserve the right to reject any PR which I feel uses a dramatically different code style. Always feel free to fork, of course, if you dislike how this project is written.

### How to Compile
If you wish to compile this project from the raw source code, simply pip install nuitka and enter the following command:
python -m nuitka --onefile --windows-icon-from-ico=CampaignChecker.ico campaign_checker.py