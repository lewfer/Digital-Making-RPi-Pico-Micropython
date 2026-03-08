# Test button input (button connected to ground)
from machine import Pin
import time

# Set up the button on pin 18 as a digital input pin
# Pull up so button value is False when pressed
switch = Pin(18, Pin.IN, Pin.PULL_UP) 

# Show the button status (True or 1 is not pressed, False or 0 is pressed)
while True:
    print(switch.value())
    time.sleep(0.01)