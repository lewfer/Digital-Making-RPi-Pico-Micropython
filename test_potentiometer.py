# Test Potentiometer
from machine import ADC
from time import sleep

#  Set up the potentiometer on pin 28 as an analogue input pin
adcpin = 28
pot = ADC(adcpin)

# Value will be 0 to 65535 (direction of increase/decrease depending on the order of black/red wires)
while True:
    # Get the raw value from 0 to 65535
    val = pot.read_u16()
    print(val, end=", ")
    
    # Convert the value to a voltage
    volt = (3.3/65535)*val
    print(round(volt,2))
    
    sleep(0.2)