# Test line following sensor on a RPi Pico

from machine import Pin
import time

# Set up the sensor
sensor = Pin(10, Pin.IN, Pin.PULL_DOWN) 


# Show the sensor status (True is light, False is dark)
while True:
    print(sensor.value())
    time.sleep(0.01)
