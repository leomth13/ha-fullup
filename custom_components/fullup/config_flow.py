"""Config flow for Fullup V2 Integration"""

from homeassistant import config_entries
import voluptuous as vol

DOMAIN = "fullup"

class FullupConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            title = user_input.pop("title", "Fullup Tanks")
            return self.async_create_entry(title=title, data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Optional("title", default="Fullup Tanks"): str,
                vol.Required("username"): str,
                vol.Required("password"): str,
            }),
        )
