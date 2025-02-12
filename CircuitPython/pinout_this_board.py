#         RESET BTN []   USB   [] BOOT BTN IO21
# RGB          GP12  ~  |___|  O  VBAT
# ADC3 I2C0SCL GP29  O         O  5V
# ADC2 I2C0SDA GP28  O         O  GND
# ACC1 I2C1SCL GP27  O         O  3.3V
# ACC0 I2C1SDA GP26  O  -----  O  GP3 I2C1SCL      SPI0TX
# U1RX I2C0SCL GP25  O | LCD | O  GP4 I2C0SDA U1TX SPI0RX
# U1TX I2C0SDA GP24  O |     | O  GP6 I2C1SDA      SPI0SCK
# U1TX I2C0SDA GP20  O  -----  O  GP5 I2C1SCL U1RX SPI0CS
#                     ---------
# OLED Screen at address I2C ['0x3c']
# OLED Screen Resolution 72x40
# OLED Chip SSD1306
#
# RGB Neopixel on GP12
#
# SH1.0 4P connector [GP23-SCL, GP22-SDA, 3.3V, GND]
#
#
# https://github.com/01Space/RP2040-0.42LCD/blob/main/image/RP2040-0.42LCD.jpg 