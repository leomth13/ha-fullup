# Fullup V2 Integration for Home Assistant ⛽️

This integration allows you to monitor your [Fullup](https://fullup.io/) fuel tank sensors in Home Assistant, using the new REST API recently launched by Fullup alongside the new client interface.

## Roadmap 🗺️

### Launch release 2026.07.2 🚀
- [x] Rebuild Fullup Integration in Home Assistant with the new REST API deployed since July 1, 2026
- [x] Ship all basic features and sensors useful for a quick and integrated look at tanks sensors
- [x] Polishing onboarding process, adding translations and keys for translations in French, Dutch, German and English

### Next features to think about
- [ ] Refining translations for better sensor naming (if needed, low-priority)
- [ ] Adding checks to prevent double entry for the same account
- [ ] More explicit errors gestion and display during onboarding
- [ ] New entities for sensors: daily consumption (depends on API fix or manual entities), days before failure,...
- [ ] Hassle-free automation system for low fuel alerts

Other suggestions are welcomed in the [Issues section](https://github.com/leomth13/ha-fullup/issues) (use a `suggestion` tag or so).

## What is Fullup?

[Fullup](https://fullup.io/) is a smart fuel tank monitoring system. It features a wireless sensor that attaches to your fuel tank and connects to the Fullup cloud service via a modem connected to your ISP router. This setup allows for real-time monitoring of your fuel levels.

## Operation and Features

This integration connects your Fullup sensors to Home Assistant, allowing you to:

- Add every sensor linked to your account in Home Assistant, if you have multiple sensors
- Monitor fuel levels in real-time (data from sensor to modem are pushed every hour, integration pulls from API every 15 minutes)
- Track fuel consumption on a 7 or 15-day average
- Monitor tank temperature
- Monitor battery levels of your Fullup sensors
- View historical data and consumption trends
- Monitor sensors communication with a Last Seen sensor, giving you the last time the sensor talked to the modem
- If connection with API is lost (Internet connection offline, API down/in maintenance,...), logs will appear and sensors will keep their last updated value until API is reachable again

## API Information

Since July 1, 2026, Fullup changed its whole IoT infrastructure (URLs, Mobile App, API,...). To use this integration (or replace the [previous one](https://github.com/zedissime/ha-fullup)), you need to get access to the Developer Portal of Fourdata (the new IoT infrastructure partner). To do this, you can email the Fullup Support at one of the following addresses:
- support@fullup.be
- migration@fullup.be

The latter worked for myself quite rapidly. Please be kind and respectful with the person you will write to, simply explain that you would like to ask for API access to use this integration.

To get more information about the API credentials and how to retrieve them, see the [api_guide.md](https://github.com/leomth13/ha-fullup/blob/master/api_guide.md) file.

### Fullup Subscription

Fullup Support clarified the new billing service associated with the [Client Portal access](client.fullup.be), which is free until January 1st, 2027. After that, a 24€ annual fee will apply. This fee applies to all services they offer, including Client Portal access, [Developer Portal access](https://auth.fourdata.io/login) (granted for free in this case of personal use), API usage, and data access from your sensors. If you want to retain access to your data and the entire new suite of tools, **you will need to pay the 24€/year fee**.

*Note that the Developer Portal is usually a paid service, but Fullup agrees to upgrade your personal account to a professional account for free in this case. This upgrade will not incur any additional fees, but to retain access to all features, the 24€ fee must be paid.*

## ⚠️ Important Note for V1 Users

This **Fullup V2** component is a complete rewrite supporting the new Fullup REST API and Home Assistant UI Configuration. If you used the old Fullup Integration or still have it installed on your system, it is important that you follow these instructions to make sure you can install and configure the new component safely:
1. Delete the old Fullup integration from HACS
2. Remove any old `fullup:` entries from your configuration.yaml file (if applicable)
3. Restart Home Assistant
4. Check that the path `/config/custom_components/fullup` (or `/homeassistant/custom_components/fullup`, depending on your installation and the root repertory name of your instance) is free. You can do this with any tool like File Editor, VS Code or even Terminal
5. Follow the installation guide below to install the new component

## Installation

### HACS Installation

1. Open HACS
2. Click the three dots in the top right corner
3. Select "Custom repositories"
4. Add the URL of the repository (https://github.com/leomth13/ha-fullup)
5. Select "Integration" as the category
6. Click "Add"
7. Return to the integrations list in HACS
8. Search for "Fullup Fuel V2 (New API)
9. Click on the integration and install it by clicking on the blue arrow in the bottom right corner or at the bottom of the rendered README page
10. Go into Settings > Confirm Restart, or Restart Home Assistant manually

### Manual Installation

1. Copy the `fullup` folder with its files to your `custom_components` directory
2. Restart Home Assistant

## Configuration

1. Go to Settings -> Devices & Services
2. Click "Add Integration"
3. Search for "Fullup Fuel"
4. Follow the onboarding and instructions provided at each step

## Available Sensors

- Current Volume (L)
- Temperature (°C)
- Battery Level (%)
- Consumption on a weekly average (7-day) (L)
- Consumption on a fortnight average (14-day) (L)
- Last Seen sensor for the latest data transmission from the device (text sensor)

## Support

For issues and feature requests, please use the [GitHub issue tracker](https://github.com/leomth13/ha-fullup/issues) or create a [Pull request](https://github.com/leomth13/ha-fullup/pulls) .

## Acknowledgment and Copyright
This repository is based on and forked from the original custom component from [zedissime](https://github.com/zedissime/ha-fullup). Description and organization of the repository are copied from it and will be modified as the development goes on.

This project is not in any case associated with Fullup or Fourdata. It only uses tools provided to develop a solution for the Home Assistant community.

©FULLUP SPRL
