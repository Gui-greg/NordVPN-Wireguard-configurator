# Wireguard Configuration Generator for NordVPN

Currently, NordVPN does not offer an official method to generate a Wireguard configuration file. This tool assists you in creating this file, which can be utilized in various applications.

## Prerequisites

- Python 3.x
- Active NordVPN subscription

## Installation

Clone this repository and navigate to the project directory to begin.

## Usage

1. Execute the startup script:
   ```bash
   ./run.sh
   ```

The script will:
- Verify Python installation
- Request your NordVPN API token
- Generate a `wg0.conf` file containing:
  - Private/Public key pair
  - Server endpoint configuration
  - Connection parameters

## Obtaining a NordVPN API Token

Visit the [NordVPN site](https://my.nordaccount.com/dashboard/nordvpn/access-tokens/) and click the `Generate new token` button. Select `Set to expire in 30 days`, click `Generate token`, and then `Copy and close` to save the token to your clipboard.

## If this script was beneficial and saved you time, consider supporting me with a coffee

https://www.paypal.com/donate/?hosted_button_id=ED85ESV6EDWV4