from machine import Pin
import time
from net import Wifi

PORT = 5000

# Create an object for the built-in LED
led = Pin("LED", Pin.OUT)

# Create a network object
wifi = Wifi()

try:
    # Connect to WIFI
    wifi.connect()

    # Create receiver to listen for messages
    wifi.createReceiver(PORT)

    # Receive messages
    while True:
        message = wifi.receiveMessage()
        print("Received", message)

        # Carry out command
        if message=="on":
            led.on()
        elif message=="off":
            led.off()


except Exception as e:
    print("Error", e)