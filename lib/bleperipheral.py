# Class to implement Bluetooth Low Energy (BLE) Peripheral functionality
# Peripheral is the sending end of the connection

from micropython import const
import asyncio
import aioble
import bluetooth

class blePeripheral:

    # Set up a Peripheral service on the given name.
    # The function provided will be called to get the latest data value.
    def __init__(self, name, fn):
        self.name = name
        
        # Set up service and characteristics
        self._SERVICE_UUID = bluetooth.UUID(0x181A) # org.bluetooth.service.environmental_sensing
        self._CHARACTERISTIC_UUID = bluetooth.UUID(0x2A6E) # org.bluetooth.characteristic.temperature
        self._APPEARANCE = const(768) # org.bluetooth.characteristic.gap.appearance.xml
        
        # How frequently to send advertising beacons.
        self._INTERVAL_MS = 250_000
    
        # Register GATT server.
        temp_service = aioble.Service(self._SERVICE_UUID)
        self.temp_characteristic = aioble.Characteristic(
            temp_service, self._CHARACTERISTIC_UUID, read=True, notify=True
        )
        aioble.register_services(temp_service)
        
        self.callback = fn

    # Convert string to bytes
    def encode_message(self, message):
        """ Encode a message to bytes """
        return message.encode('utf-8')
        
    # Poll the data from the registered callback and send it to the central
    async def data_task(self):
        while True:
            message = self.callback()
            self.temp_characteristic.write(self.encode_message(message), send_update=True)
            await asyncio.sleep_ms(100)


    # Wait for connections. 
    async def peripheral_task(self):
        while True:
            print("BLE waiting for connection...")
            async with await aioble.advertise(
                self._INTERVAL_MS,
                name=self.name,
                services=[self._SERVICE_UUID],
                appearance=self._APPEARANCE,
            ) as connection:
                print("Connection from", connection.device)
                await connection.disconnected(timeout_ms=None) # wait for disconnect before advertising again


    # Run both tasks.
    async def main(self):
        t1 = asyncio.create_task(self.data_task())
        t2 = asyncio.create_task(self.peripheral_task())
        await asyncio.gather(t1, t2)
        
    def run(self):
        asyncio.run(self.main())


