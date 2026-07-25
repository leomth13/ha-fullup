"""Sensor Configuration for Fullup V2 Integration"""
import base64
from datetime import timedelta
import logging

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PERCENTAGE, UnitOfTemperature, UnitOfVolume
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)

_LOGGER = logging.getLogger(__name__)
DOMAIN = "fullup"
SCAN_INTERVAL = timedelta(minutes=15)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
):
    username = entry.data["username"]
    password = entry.data["password"]

    async def update_data():
        auth = base64.b64encode(f"{username}:{password}".encode()).decode()
        headers = {"Authorization": f"Basic {auth}", "accept": "application/json"}
        try:
            session = async_get_clientsession(hass)
            url = "https://pro-api.fuel-it.io/v2/contenant/allassets"
            async with session.get(url, headers=headers, timeout=15) as resp:
                if resp.status == 200:
                    return await resp.json()
                else:
                    raise UpdateFailed(f"API error (Status: {resp.status})")
        except Exception as e:
            raise UpdateFailed(f"Connection to API failed. Details: {e}")

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=DOMAIN,
        update_method=update_data,
        update_interval=SCAN_INTERVAL,
    )
    await coordinator.async_config_entry_first_refresh()

    entities = []
    assets = coordinator.data or []

    for asset in assets:
        if not isinstance(asset, dict):
            continue

        device_name = asset.get("name", "Unknown Tank")
        uid = asset.get("uid")
        devices = asset.get("devices") or [{}]
        device = devices[0] if devices else {}

        device_info = DeviceInfo(
            identifiers={(DOMAIN, uid)},
            name=device_name,
            manufacturer="Fullup / Four Data",
            model=device.get("referential", "Tekelek"),
            sw_version=device.get("software_version"),
        )

        entities.append(FullupVolumeSensor(coordinator, asset, device_info))
        entities.append(FullupConsumptionSensor(coordinator, asset, "7", device_info))
        entities.append(FullupConsumptionSensor(coordinator, asset, "15", device_info))
        entities.append(FullupBatterySensor(coordinator, asset, device_info))
        entities.append(FullupTemperatureSensor(coordinator, asset, device_info))
        entities.append(FullupLastSeenSensor(coordinator, asset, device_info))

    async_add_entities(entities)


class BaseFullupSensor(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name = True
    def __init__(self, coordinator, asset, device_info):
        super().__init__(coordinator)
        self._asset = asset
        self._attr_device_info = device_info
        self._attr_unique_id = f"fullup_{asset.get('uid')}_{self._sensor_type}"

        devices = asset.get("devices") or [{}]
        device = devices[0] if devices else {}
        self._attr_extra_state_attributes = {
            "uid": asset.get("uid"),
            "device_number": device.get("number"),
            "internal_reference": asset.get("internal_reference"),
        }

    @property
    def available(self) -> bool:
        return True

    @property
    def should_poll(self) -> bool:
        return False


class FullupVolumeSensor(BaseFullupSensor):
    _sensor_type = "remaining_volume"
    _attr_translation_key = "remaining_volume"
    _attr_native_unit_of_measurement = UnitOfVolume.LITERS
    _attr_device_class = SensorDeviceClass.VOLUME_STORAGE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 0

    @property
    def native_value(self):
        for a in self.coordinator.data or []:
            if a.get("uid") == self._asset.get("uid"):
                return a.get("volume")
        return None


class FullupConsumptionSensor(BaseFullupSensor):
    def __init__(self, coordinator, asset, days, device_info):
        self._days = days
        self._sensor_type = f"consumption_{days}d"
        self._attr_translation_key = f"consumption_{days}d"
        super().__init__(coordinator, asset, device_info)

        self._attr_native_unit_of_measurement = UnitOfVolume.LITERS
        self._attr_state_class = SensorStateClass.TOTAL
        self._attr_suggested_display_precision = 0

    @property
    def native_value(self):
        for a in self.coordinator.data or []:
            if a.get("uid") == self._asset.get("uid"):
                return a.get(f"consumption_{self._days}_days")
        return None


class FullupBatterySensor(BaseFullupSensor):
    _sensor_type = "battery"
    _attr_translation_key = "battery"
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def native_value(self):
        for a in self.coordinator.data or []:
            if a.get("uid") == self._asset.get("uid"):
                devices = a.get("devices") or []
                if devices:
                    return devices[0].get("battery")
        return None


class FullupTemperatureSensor(BaseFullupSensor):
    _sensor_type = "temperature"
    _attr_translation_key = "temperature"
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 0

    @property
    def native_value(self):
        for a in self.coordinator.data or []:
            if a.get("uid") == self._asset.get("uid"):
                temps = a.get("last_data", {}).get("temperatures", [])
                return temps[0] if temps else None
        return None


class FullupLastSeenSensor(BaseFullupSensor):
    _sensor_type = "last_seen"
    _attr_translation_key = "last_seen"

    @property
    def native_value(self):
        for a in self.coordinator.data or []:
            if a.get("uid") == self._asset.get("uid"):
                devices = a.get("devices") or []
                if devices:
                    return devices[0].get("date_last_seen")
        return None
