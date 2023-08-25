# Example of how to connect to WiFi and call an API

from network_manager import NetworkManager
import uasyncio
from urllib import urequest
import WIFI_CONFIG
import json
import time

# URL of the API
URL = "https://official-joke-api.appspot.com/random_joke"

# Function to handle status messages
def status_handler(mode, status, ip):
    print(mode, status, ip)
    
# Connect to WiFi
network_manager = NetworkManager(WIFI_CONFIG.COUNTRY, status_handler=status_handler)
uasyncio.get_event_loop().run_until_complete(network_manager.client(WIFI_CONFIG.SSID, WIFI_CONFIG.PSK))

# Call the api
socket = urequest.urlopen(URL)

# Decode the response and display the joke
d = json.load(socket)
print(d["setup"])
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(d["punchline"])


