"""Fullup V2 Integration"""
import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

DOMAIN = "fullup"
PLATFORMS = ["sensor"]

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Initial setup via YAML (Deprecated in V2)."""
    if DOMAIN in config:
        _LOGGER.warning(
            "Configuration of Fullup via configuration.yaml is deprecated (V2). "
            "Please remove these lines from your YAML file and configure the integration "
            "via Settings -> Devices & Services."
        )
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Fullup from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
