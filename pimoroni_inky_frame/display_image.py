# Example to show displaying an image on the Inky Frame

# Select the correct library for your screen size: DISPLAY_INKY_FRAME_4 for 4", DISPLAY_INKY_FRAME_7 fo 7.3" and DISPLAY_INKY_FRAME for 5.7"
from picographics import PicoGraphics, DISPLAY_INKY_FRAME_4 as DISPLAY
#from picographics import PicoGraphics, DISPLAY_INKY_FRAME as DISPLAY
#from picographics import PicoGraphics, DISPLAY_INKY_FRAME_7 as DISPLAY

from jpegdec import JPEG

graphics = PicoGraphics(DISPLAY)

# Load the file 
j = JPEG(graphics)
j.open_file("cow.jpg")
j.decode()

# Display it
graphics.update()
