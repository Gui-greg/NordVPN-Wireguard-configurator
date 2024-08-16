# Wireguard Configuration Generator for NordVPN

Currently, NordVPN does not offer an official method to generate a Wireguard configuration file. This tool assists you in creating this file, which can be utilized in various applications.

For this process, you will need:
- A terminal with Python 3 installed
- An active NordVPN subscription
- An internet connection

The tool requires a single input: the access token. This token is used to retrieve the NordLynx private key.

To obtain this token, go to the [NordVPN site](https://my.nordaccount.com/dashboard/nordvpn/manual-configuration/), click on the `Generate new token` button. Choose `Doesn't expire` and click `Generate token`, then `Copy and close`. This action will save the token to your clipboard.

Next, run the command: `./generate_config.py <YOUR_TOKEN>` in your terminal, replacing `<YOUR_TOKEN>` with the actual token you copied earlier.
If everything works correctly, you will see a message like: `Successfully created a WireGuard config for server: <NordVPN Country> #<Server number>`.

You will now have a `wg0.conf` file, complete with all necessary settings, ready for use.

## Possible issues

- Error message: `env: python3: No such file or directory`
    - Possible cause: python3 is not installed on your machine.
    - Solution: Try running the command like this: `python generate_config.py <YOUR_TOKEN>`. If this still fails probably no python is installed on your machine.


## If this script was beneficial and saved you time, consider supporting me with a coffee

https://www.paypal.com/donate/?hosted_button_id=ED85ESV6EDWV4