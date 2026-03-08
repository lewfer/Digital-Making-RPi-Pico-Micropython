# Test neopixel

import machine, neopixel
import time

# Define a neopixel on pin 4 with 8 pixels
np = neopixel.NeoPixel(machine.Pin(4), 8)

# Set the colour of the first 3 neopixels
np[0] = (255, 0, 0) # set to red, full brightness
np[1] = (0, 128, 0) # set to green, half brightness
np[2] = (0, 0, 64)  # set to blue, quarter brightness

np.write()