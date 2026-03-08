from machine import Pin, I2C
from time import sleep
import bme280

# Set up i2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)

# Set up weather sensor
bme = bme280.BME280(i2c=i2c)

while True:
  print('Temperature: ', bme.temperature)
  print('Humidity: ', bme.humidity)
  print('Pressure: ', bme.pressure)

  sleep(2)