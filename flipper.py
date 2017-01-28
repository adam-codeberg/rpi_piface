#!/bin/python
'''
"Flip Clock" effect when printing string to LCD
'''

import pifacecad
import time
import string

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
    for char in txt:
        for item in char_list:
            if item == char:
                pos = char_list.index(char)
                select = char_list[pos-steps:pos+1]
                display_list.append(select)
    return display_list

def write_flip_list(txt, steps, delay):
    flip_list = get_flip_list(txt, steps)
    print(flip_list)
    speed = delay
    for item in flip_list:
        for char in item:
            if char is item[-1]:
                cad.lcd.write(char)
            else:
                cad.lcd.write(char)
                cursor = cad.lcd.get_cursor()
                cad.lcd.set_cursor(cursor[0]-1, cursor[1])
                speed *= 0.5
            print(speed)
            time.sleep(speed)

# Example useage
write_flip_list('Hello world! :)', 4, 1.0) # eg: foo(string, steps, delay)
