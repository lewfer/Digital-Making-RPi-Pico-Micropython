# Mount the SD card

# Set up the SD card
import gc
import uos
import sdcard  # noqa: E402 - putting this at the top causes an MBEDTLS OOM error!?
sd_spi = machine.SPI(0, sck=machine.Pin(18, machine.Pin.OUT), mosi=machine.Pin(19, machine.Pin.OUT), miso=machine.Pin(16, machine.Pin.OUT))
sd = sdcard.SDCard(sd_spi, machine.Pin(22))
uos.mount(sd, "/sd")
gc.collect()  # Claw back some RAM!
