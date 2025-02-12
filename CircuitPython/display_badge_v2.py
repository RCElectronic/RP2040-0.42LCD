import board
import busio
import displayio
import time

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

# Draw a label

line1 = label.Label(terminalio.FONT, text=" "*6,
                         color=0xFFFF00,
                         scale = 2,
                         x=0, y=8)
splash.append(line1)


line2 = label.Label(terminalio.FONT, text=" "*6,
                         color=0xFFFF00,
                         scale = 2,
                         x=0, y=28)
splash.append(line2)

while True:
    line1.text = "Time:"
    line2.text = "{:>6}".format(time.monotonic()) #right aligned

    time.sleep(1)
    pass
