# Blink the built-in LED

from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

for i in range(10):
    led.on()
    sleep(1)
    led.off() 
    sleep(1)
