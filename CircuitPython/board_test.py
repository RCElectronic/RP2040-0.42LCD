# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Added code for RGB pixel, screen dimensions (72x40) and small changes to
# function with CircuitPython 9.x.x
# Use the regular Pico board uf2: https://circuitpython.org/board/raspberry_pi_pico/
# Download the library bundle and copy the modules into the lib folder on the pico
# (You may need to create a lib folder):
# neopixel.mpy
# adafruit_display_text (folder)
# adafruit_displayio_ssd1306.mpy 

"""
This test will initialize the display using displayio and draw a solid white
background, a smaller black rectangle, another black to clear for text,
and some white text. 
"""

import board
import busio  
import displayio
import neopixel
from rainbowio import colorwheel
import time

try:
    from i2cdisplaybus import I2CDisplayBus
except ImportError:
    from displayio import I2CDisplay as I2CDisplayBus

import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

#i2c = busio.I2C(board.SCL, board.SDA)
i2c = busio.I2C(board.GP23, board.GP22)
display_bus = I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=72, height=40)

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(72, 40, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(62, 32, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
splash.append(inner_sprite)

# Draw a thin inner rectangle for text background
inner_bitmap = displayio.Bitmap(72, 10, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=0, y=15)
splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=2, y=20)
splash.append(text_area)

num_pixels = 1
pixels = neopixel.NeoPixel(board.GP12, num_pixels, auto_write=False)
pixels.brightness = 0.1

def rainbow(speed):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(speed)

while True:
    rainbow(.1)

