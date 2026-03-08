# Test PWM brightness control on an LED
from machine import Pin, PWM
import time

# Set up the LED on pin 13 as an analogue output pin
led = PWM(Pin(13))
led.freq (1000)

while True:
      # Increase the duty cycle gradually
      for brightness in range(0, 65536, 2000):
        led.duty_u16(brightness)
        time.sleep(0.1)