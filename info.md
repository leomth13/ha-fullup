## Changelog

### Version 2026.07.1

#### First Version

- Adds every tank sensor you own in separate devices, under one unified config entry
- For each device, creates multiple sensors:
- Volume (in L)
- Cavitiy/Sensor temperature
- Battery percentage
- Fuel consumption of the week (7-day average)
- Fuel consumption of the fortnight (14-day average)
- Last Seen sensor for each device, letting you know when the sensor itself has transmitted data for the last time
- Automatically pulls from the API at a fixed frequency (15 minutes). _Note: max API usage is 10 calls per rolling hour, sensor updates every hour so this is, to me, the optimal frequency, considering calls made every start/restart._ 
### Installation

- Recommended via HACS
- Add the repository URL in your Custom Repositories in HACS > 3 dots in the upper-right corner > Custom repositories
- Restart Home Assistant after installing or updating. Updating via HACS is recommended

### Support

For any issues or suggestions, please open an issue on the GitHub repository.
