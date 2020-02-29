#!/usr/bin/env python


import i2c_driver
import time


mylcd = i2c_driver.LCD()

mylcd.lcd_display_string("Hello World", 1)
mylcd.lcd_display_string("My name is Kevin", 2)

#while True:
#    mylcd.lcd_display_string(time.strftime('%I:%M:%S %p'), 1)
#    mylcd.lcd_display_string(time.strftime('%a %b %d, 20%y'), 2)
