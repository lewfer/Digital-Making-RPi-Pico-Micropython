# Test LDR (Light Dependent Resistor, sometimes called a photocell)

from machine import ADC
from time import sleep

#  Set up the LDR on pin 28 as an analogue input pin
adcpin = 28
pot = ADC(adcpin)

# Value will be 0 to 65535 (0 for bright, 65535 for dark or vice versa depending on the order of black/red wires)
while True:
    val = pot.read_u16()
    print(val)
    time.sleep(0.2)