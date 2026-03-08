# Test PIR (Passive Infra-Red detector)

from machine import Pin
import time

# Set up the button on pin 16 as a digital input pin
pir = Pin(19, Pin.IN, Pin.PULL_DOWN)           

# Wait for intruders
while True:
    if pir.value():
        print("Intruder!")
        while pir.value():
            pass
    print("Waiting")
    time.sleep(0.1)

