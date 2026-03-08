# Test button input (button connected to 3V3)
from machine import Pin
import time

# Set up the button on pin 18 as a digital input pin
# Pull down so button value is True when pressed
switch = Pin(18, Pin.IN, Pin.PULL_DOWN) 

# Show the button status (True or 1 is pressed, False or 0 is not pressed)
while True:
    print(switch.value())
    time.sleep(0.01)
    