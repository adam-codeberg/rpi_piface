#!/bin/python
'''
Writes string to PiFace Control and Display
hat for RaspberryPi, as a non-sequential
flipper. Enjoy!

Written in: Python 3.6.0
'''
__author__ = 'https://github.com/adam-codeberg'
__status__ = 'Development' 

import pifacecad
import time
import string
import random

cad = pifacecad.PiFaceCAD()
cad.lcd.clear()
cad.lcd.backlight_on() 

def get_flip_list(txt, steps):
    char_list =  ( list(string.ascii_uppercase) + \
                   list(string.ascii_lowercase) + \
                   list(' ') + \
                   list(string.digits) + \
                   list(string.punctuation) )
    display_list = []
    count = 0
    for char in txt:
        for item in char_list:
            if item == char:
                pos = char_list.index(char)
                select = char_list[pos-steps:pos+1]
                display_list.append({'col': count, 'data' : select})
                count += 1
    result = random.sample(display_list, len(display_list))
    return result


def write_flip_list(txt, steps, delay):
    flip_list = get_flip_list(txt, steps)
    flip_list_index = list(range(len(flip_list)))
    speed = delay
    for d in flip_list:
        for k,v in d.items():
            if 'data' in k:
                for char in v:
                    cad.lcd.set_cursor(d['col'], 0)
                    cad.lcd.write(char)
            time.sleep(speed)
    cad.lcd.set_cursor(len(flip_list), 0)
write_flip_list('Hello world! :)', 4, 0.01)
