# Hardware Used: Raspberry Pi 4b+, Raspberry Pi sense hat
# Code is copied but modified from the online tutorial: Sense Hat Random Sparkles by Raspberry pi
# Link: https://projects.raspberrypi.org/en/projects/sense-hat-random-sparkles/3

from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
x=0
y=0
x2=7
y2=7
x3= 0
y3=7
x4=7
y4=0
r= randint(100,255) #100,255 range to make it more pastel coloured
g= randint(100,255)
b= randint(100,255)

sense.set_pixel(x, y, r, g, b)
sense.set_pixel(x2, y2, r, g, b)
sense.set_pixel(x3, y3, r, g, b)
sense.set_pixel(x4, y4, r, g, b)
