# Test sending BLE messages as a peripheral to a controller

from bleperipheral import blePeripheral
import random

def setMessage():
    return random.choice(["hello","bye","wow!",""])

ble = blePeripheral("my peripheral", setMessage)
ble.run()
