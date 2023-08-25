# Example to show displaying an image from the SD card on the Inky Frame

# Select the correct library for your screen size: DISPLAY_INKY_FRAME_4 for 4", DISPLAY_INKY_FRAME_7 fo 7.3" and DISPLAY_INKY_FRAME for 5.7"
from picographics import PicoGraphics, DISPLAY_INKY_FRAME_4 as DISPLAY
#from picographics import PicoGraphics, DISPLAY_INKY_FRAME as DISPLAY
#from picographics import PicoGraphics, DISPLAY_INKY_FRAME_7 as DISPLAY

from jpegdec import JPEG

# Set up the SD card
import gc
import uos
import sdcard  # noqa: E402 - putting this at the top causes an MBEDTLS OOM error!?
sd_spi = machine.SPI(0, sck=machine.Pin(18, machine.Pin.OUT), mosi=machine.Pin(19, machine.Pin.OUT), miso=machine.Pin(16, machine.Pin.OUT))
sd = sdcard.SDCard(sd_spi, machine.Pin(22))
uos.mount(sd, "/sd")
gc.collect()  # Claw back some RAM!


graphics = PicoGraphics(DISPLAY)

# Load the file 
j = JPEG(graphics)
j.open_file("/sd/cow.jpg")
j.decode()

# Display it
graphics.update()
