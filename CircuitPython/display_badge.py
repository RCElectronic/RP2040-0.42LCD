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

line1 = label.Label(terminalio.FONT, text=" "*12,
                         color=0xFFFF00,
                         x=0, y=4)
splash.append(line1)
line1.text = "abcdefghijkl"

line2 = label.Label(terminalio.FONT, text=" "*12,
                         color=0xFFFF00,
                         x=0, y=14)
splash.append(line2)
line2.text = "012345678901"

line3 = label.Label(terminalio.FONT, text=" "*12,
                         color=0xFFFF00,
                         x=0, y=24)
splash.append(line3)
line3.text = "ABCDEFGHIJKL"

line4 = label.Label(terminalio.FONT, text=" "*12,
                         color=0xFFFF00,
                         x=0, y=34)
splash.append(line4)
line4.text = "`!@#$%^&*()-"

while True:
    line1.text = "Time:"
    line2.text = "{:>12}".format(time.monotonic()) #right aligned
    line3.text = ""
    line4.text = ""
    time.sleep(1)
    pass
