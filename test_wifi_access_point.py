# Test wifi access point on a RPi Pico

from net import Wifi

# Create a network object
wifi =  Wifi()

# Create a wireless access point, providing the SSID and password
wifi.startWifiAccessPoint("mypico","hello")


