# Test blinking of an LED
from machine import Pin
import time

# Set up the LED on pin 16 as a digital output pin
led = Pin(16, Pin.OUT)

# Loop forever, blinking the LED
while True:
    led.on()           # or can use led.value(1)
    time.sleep(0.5)
    led.off()          # or can use led.value(0)
    time.sleep(0.5)