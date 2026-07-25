"""Fullup V2 Integration"""
import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

DOMAIN = "fullup"
PLATFORMS = ["sensor"]

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Configuration initiale via YAML (obsolète pour la V2)."""
    if DOMAIN in config:
        _LOGGER.warning(
            "La configuration de Fullup via configuration.yaml est obsolète (V2). "
            "Veuillez supprimer ces lignes de votre fichier YAML et configurer l'intégration "
            "directement via l'interface : Paramètres -> Appareils et services."
        )
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Initialisation d'une instance configurée via l'interface UI."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Déchargement d'une instance."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
