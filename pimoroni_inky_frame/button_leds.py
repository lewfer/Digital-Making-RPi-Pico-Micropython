# Example to show reading of buttons and lighting button LEDs

import inky_frame
import time

# Turn on LED A, dim it, then turn it off
inky_frame.button_a.led_on()
time.sleep(1)
inky_frame.button_a.led_brightness(0.66)
time.sleep(1)
inky_frame.button_a.led_brightness(0.33)
time.sleep(1)
inky_frame.button_a.led_off()

# Read the button status and toggle the leds
while True:
    if inky_frame.button_a.read():
        inky_frame.button_a.led_toggle()
        
    if inky_frame.button_b.read():
        inky_frame.button_b.led_toggle()
        
    if inky_frame.button_c.read():
        inky_frame.button_c.led_toggle()
        
    if inky_frame.button_d.read():
        inky_frame.button_d.led_toggle()
                
    if inky_frame.button_e.read():
        inky_frame.button_e.led_toggle()