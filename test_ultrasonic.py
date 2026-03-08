# Test ultrasonic distance sensor

from hcsr04 import HCSR04
import time

sensor = HCSR04(trigger_pin=6, echo_pin=7)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    time.sleep(0.5)
