# Test receiving BLE messages as a controller from a peripheral

from blecentral import bleCentral


def receivedMessage(message):
   print("Recieved ", message)
     
ble = bleCentral("my peripheral", receivedMessage)
ble.run()
