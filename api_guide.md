# How to get API keys with the new Fullup Interface

## ⚠️ Important note on Fullup Subscription ⚠️

Fullup Support clarified the new billing service associated with the [Client Portal access](client.fullup.be), which is free until January 1st, 2027. After that, a 24€ annual fee will apply. This fee applies to all services they offer, including Client Portal access, [Developer Portal access](https://auth.fourdata.io/login) (granted for free in this case of personal use), API usage, and data access from your sensors. If you want to retain access to your data and the entire new suite of tools, **you will need to pay the 24€/year fee**.

*Note that the Developer Portal is usually a paid service, but Fullup agrees to upgrade your personal account to a professional account for free in this case. This upgrade will not incur any additional fees, but to retain access to all features, the 24€ fee must be paid.*

## Client Interface and Developer Interface
Since July 1 2026, Fullup migrated its IoT systems to a new set of tools. Mobile app, URLs and API used in the past are now deprecated and replaced by a whole new suite in collaboration with Fourdata. If you migrated correctly your account
(you got at least 2 emails from Fullup regarding this matter), you should have access to the *Client Interface* available at https://client.fullup.be.

This interface doesn't provide API settings. For that you will need to get access to the *Developer Interface*, available at https://auth.fourdata.io after getting in touch with Fullup Support. You may reach them by email (support@fullup.be or migration@fullup.be) or directly via the
[contact form](https://fullup.io/contact/). In your request, you can ask for a personal access to the Developer Interface to get your API credentials in order to use this integration. Please be patient and kind towards the Support.

Once you get access to the Developer Interface, you may proceed with the instructions provided by the support (they attach several screenshots to show you in your account where to go) or double-check with the instructions below.

## Developer Interface Walkthrough: How to obtain your API keys

Once you have access to the [Developer Interface](https://auth.fourdata.io), simply navigate to it and log in with your Fullup account. On the left, go to **Settings** (the last item of the menu bar), then click on the **API** box in the upper banner of this page. You will see a few interesting options under this section: *Documentation* (which can be helpful if you want to test things out, search for new capabilities to suggest, or simply test your API keys), *Your API key* box and *API limit counter* box. **An API key is already conofigured in the API key box, it is completely normal since the Fullup Support has technically created one for the demo pictures they normally sent you in response to your query**. Select **RESET** on the left of the API key box, and you will be warned that the API keys will be revoked when resetting and a new set of keys will be displayed. When you get the pop-up with your new API username and API key/password, **please copy them somewhere safe**, as the username will only appear once here and won't be displayed again. If you don't save or lose your API username, you will need to *reset your API keys again*.

After saving your credentials, you can close the pop-up/validate the action to get back to the API tab. Now you can go on your Home Assistant instance and follow the instructions for the installation, which are found in the [README section](https://github.com/leomth13/ha-fullup#readme).
