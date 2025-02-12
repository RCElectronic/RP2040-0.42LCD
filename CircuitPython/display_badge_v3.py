import board
import busio
import displayio
import time

from adafruit_display_shapes.roundrect import RoundRect # more with shapes library

# Compatibility with 9.x.x.
try:
    from i2cdisplaybus import I2CDisplayBus
except ImportError:
    from displayio import I2CDisplay as I2CDisplayBus

import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

scrn_wid = 72
scrn_hgt = 40

#i2c = busio.I2C(board.SCL, board.SDA)
i2c = busio.I2C(board.GP23, board.GP22)
display_bus = I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=scrn_wid, height=scrn_hgt)

# Make the display context
splash = displayio.Group()
display.root_group = splash

# Draw a rounded rectangle
badge = RoundRect(0, 0, scrn_wid, scrn_hgt, r = 4, fill=0x0, outline=0xFFFFFF, stroke=1)
splash.append(badge)


while True:
    pass
