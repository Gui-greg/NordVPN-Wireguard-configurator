#!/usr/bin/env python33

import sys
import urllib.request
import json
import base64

credentials_url = "https://api.nordvpn.com/v1/users/services/credentials"
recommendations_url = r"https://api.nordvpn.com/v1/servers/recommendations?&filters\[servers_technologies\]\[identifier\]=wireguard_udp&limit=1"
config_template_path = "wireguard_config.template"
output_config_path = "wg0.conf"

if len(sys.argv) < 2:
    print("Token was not provided! Usage: python fetch.py <API_TOKEN>")
    sys.exit(1)

api_token = sys.argv[1]

encoded_token = base64.b64encode(f"token:{api_token}".encode()).decode()
auth_headers = {"Authorization": f"Basic {encoded_token}"}

def terminate_program(msg):
    print(msg)
    print("Program is terminating!")
    exit(1)

def fetch_data(url, headers):
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request) as response:
            data = response.read()
            return json.loads(data.decode())
    except urllib.error.URLError as e:
        terminate_program(f"Failed to fetch data: {e.reason}")

credentials_response = fetch_data(credentials_url, auth_headers)
private_key = credentials_response.get("nordlynx_private_key")
if not private_key:
    terminate_program(f"Credentials failed to retrieve. Response: {credentials_response}")
print("Successfully retrieved the private key from NordVPN.")

recommended_server_response = fetch_data(recommendations_url, {})
if not recommended_server_response[0].get("name"):
    terminate_program(f"Recommended server failed to retrieve. Response: {recommended_server_response}")
server = recommended_server_response[0]
server_name = server["name"]
server_ip = server["station"]
wireguard_technology = next((tech for tech in server["technologies"] if tech["identifier"] == "wireguard_udp"), None)

if not wireguard_technology:
    terminate_program("WireGuard UDP not supported by the server.")

public_key = next((item["value"] for item in wireguard_technology["metadata"] if item["name"] == "public_key"), None)
if not public_key:
    terminate_program("Public key not found in WireGuard UDP technology.")

with open(config_template_path, "r") as file:
    config_template = file.read()

config = config_template.format(private_key=private_key, public_key=public_key, server_ip=server_ip)

with open(output_config_path, "w") as file:
    file.write(config)

print(f"Successfully created a WireGuard config for server: {server_name}")