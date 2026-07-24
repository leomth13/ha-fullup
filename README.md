# Fullup Integration for Home Assistant

This integration allows you to monitor your [Fullup](https://fullup.io/) fuel tank sensors in Home Assistant.

## What is Fullup?

[Fullup](https://fullup.io/) is a smart fuel tank monitoring system that helps you track fuel levels in your heating oil, diesel, or other liquid storage tanks. The system consists of a wireless sensor that attaches to your tank and connects to the Fullup cloud service, providing real-time monitoring of your fuel levels.

## What does this integration do?

This integration connects your Fullup sensors to Home Assistant, allowing you to:

- Monitor fuel levels in real-time
- Get alerts when fuel levels are low
- Track fuel consumption patterns
- Monitor tank temperature to prevent freezing
- Keep track of battery levels in your Fullup sensors
- View historical data and consumption trends
- Manage multiple tanks from a single dashboard

## Features

- Monitor fuel level in your tanks
- Track temperature
- Battery level monitoring
- Historical data tracking
- Multiple tanks support

## API Information

Since July 1st 2026, Fullup changed its whole IoT infrastructure (URLs, Mobile App, APIs,...). To use this integration (or replace the [previous one](https://github.com/zedissime/ha-fullup)), you need to get access to the Developer Portal of Fourdata (the new IoT infrastructure partner). To do this, you can email the Fullup Support at one of the following addresses:
- support@fullup.be
- migration@fullup.be

The latter worked for myself quite rapidly. Please be kind and respectful with the person you will write to, simply explain that you would like to ask for API access to use this integration.

_Note for the future: We still need Fullup support to clarify the new billing service associated with the [Client Portal access](client.fullup.be), which is free until January 1st 2027, after that you will need to pay a 24€ fee per year. This apparently doesn't relate to the [Developer Portal access](https://auth.fourdata.io/login), which is granted for free in this case of personal use. Still, if a fair policy consists in a certain fee to keep access to the API, it will be indicated on this page_


## Installation

### HACS Installation

1. Open HACS
2. Click the three dots in the top right corner
3. Select "Custom repositories"
4. Add the URL of your repository
5. Select "Integration" as the category
6. Click "Add"
7. Return to the integrations list in HACS
8. Search for "Fullup Fuel V2 (New API)
9. Click on the integration and install it by clicking on the blue arrow in the bottom right corner or at the bottom of the rendered README page
10. Go into Settings > Confirm Restart or Restart Home Assistant manually



### Manual Installation

1. Copy the `fullup` folder to your `custom_components` directory
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

For issues and feature requests, please use the [GitHub issue tracker](https://github.com/leomth13/ha-fullup/issues).

## Acknowledgment
This repository is based on and forked from the original custom component from [zedissime](https://github.com/zedissime/ha-fullup). Description and organization of the repository are copied from it and will be modified as the development goes on.
