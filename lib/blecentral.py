# Class to implement Bluetooth Low Energy (BLE) Central functionality
# Central is the receiving end of the connection

from micropython import const
import asyncio
import aioble
import bluetooth

class bleCentral:

    # Set up a Central service on the given name
    # The function provided will be called to share the data receieved
    def __init__(self, name, fn):
        self.name = name

        # Set up service and characteristics
        self._SERVICE_UUID = bluetooth.UUID(0x181A) # org.bluetooth.service.environmental_sensing
        self._CHARACTERISTIC_UUID = bluetooth.UUID(0x2A6E) # org.bluetooth.characteristic.temperature
        self.callback = fn

    # Convert bytes received to string
    def decode_message(self, message):
        """ Decode a message from bytes """
        return message.decode('utf-8')
        
    # Scan for devices
    async def ble_scan(self):
        # Scan for 5 seconds, in active mode, with very low interval/window (to maximise detection rate).
        async with aioble.scan(5000, interval_us=30000, window_us=30000, active=True) as scanner:
            async for result in scanner:
                # See if it matches our name and the service.
                if result.name() == self.name and self._SERVICE_UUID in result.services():
                    return result.device
        return None

    # Connect and receive messages
    async def main(self):
        # Try to find our peripheral device
        device = await self.ble_scan()
        if not device:
            print(f"Peripheral '{self.name}' not found")
            return
        print(f"Peripheral '{self.name}' found")
        self.callback("#FOUND")
        
        # Try to connect to it
        try:
            print("Connecting to", device)
            connection = await device.connect()
        except asyncio.TimeoutError:
            print("Timeout during connection")
            return
        print(f"Connected to '{self.name}'")
        self.callback("#CONNECTED")
        
        # Read data from it
        async with connection:
            try:
                service = await connection.service(self._SERVICE_UUID)
                characteristic = await service.characteristic(self._CHARACTERISTIC_UUID)
            except asyncio.TimeoutError:
                print("Timeout discovering services/characteristics")
                return
            self.callback("#READY")
            
            # Read data and send back to the registered callback
            while connection.is_connected():
                data = await characteristic.read()
                if data:
                    message = self.decode_message(data)
                    self.callback(message)
                    await asyncio.sleep_ms(100)

    # Start the service
    def run(self):  
        asyncio.run(self.main())



