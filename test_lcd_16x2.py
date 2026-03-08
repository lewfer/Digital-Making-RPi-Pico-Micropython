# Test 16x2 LCD display

from machine import Pin, SoftI2C
from pico_i2c_lcd import I2cLcd
from time import sleep

# Specify the I2C connections on the Pico
I2C_SDA = 4
I2C_SCL = 5

# Specify the LCD's i2C address (check with the i2c_scanner.py to find address)
I2C_ADDR = 0x27

# Specify the size of the LCD (2x16 or 4x20)
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Initialize I2C and LCD objects
i2c = SoftI2C(sda=Pin(I2C_SDA), scl=Pin(I2C_SCL), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# Display some text
lcd.putstr("Hello")
lcd.move_to(0, 1)
lcd.putstr("World")

# Run through other options
sleep(1)
lcd.show_cursor()
sleep(1)
lcd.hide_cursor()
sleep(1)
lcd.blink_cursor_on()
sleep(1)
lcd.blink_cursor_off()  
sleep(1)
lcd.backlight_off()
sleep(1)
lcd.backlight_on()
sleep(1)
lcd.display_off()
sleep(1)
lcd.display_on()
sleep(1)
lcd.clear()
