# Example to show drawing text and graphics on the Inky Frame

# from picographics import PicoGraphics, DISPLAY_INKY_FRAME as DISPLAY      # 5.7"
from picographics import PicoGraphics, DISPLAY_INKY_FRAME_4 as DISPLAY  # 4.0"
#from picographics import PicoGraphics, DISPLAY_INKY_FRAME_7 as DISPLAY  # 7.3"

# Set up graphics
graphics = PicoGraphics(DISPLAY)
WIDTH, HEIGHT = graphics.get_bounds()

# Colour numbers
BLACK = 0
WHITE = 1
GREEN = 2
BLUE = 3
RED = 4
YELLOW = 5
ORANGE = 6
TAUPE = 7

# Clear screen
graphics.set_pen(WHITE)
graphics.clear()

# Draw text
graphics.set_pen(BLACK)
graphics.set_font("bitmap8")
SCALE = 4
graphics.text("Hello World", 0, 0, WIDTH, SCALE)

# Draw shapes
THICKNESS = 2
graphics.line(50, 50, 80, 60, THICKNESS)
graphics.circle(80, 80, 10)
graphics.rectangle(100, 100, 50, 20)
graphics.triangle(150, 150, 160, 150, 190, 190)

# Display it
graphics.update()

