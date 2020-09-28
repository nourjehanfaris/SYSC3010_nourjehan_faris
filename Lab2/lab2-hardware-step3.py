# Hardware Used: Raspberry Pi 4b+, Raspberry Pi sense hat
# Code is copied but modified from the online tutorial: Sense Hat Random Sparkles by Raspberry pi
# Link: https://projects.raspberrypi.org/en/projects/sense-hat-random-sparkles/3

from sense_hat import SenseHat
from random import randint
from time import sleep

count=0 #added a counter to clear a random pixel

while True:
    if count%2==0:
        sense = SenseHat()
        x=randint(1,6) 
        y=randint(1,6)
        r= randint(100,255) #100,255 range to make it more pastel coloured
        g= randint(100,255)
        b= randint(100,255)

        sense.set_pixel(x, y, r, g, b)
        count +=1
        sleep(0.005) #faster pixels
    else:
        
        sense = SenseHat()
        x=randint(1,6) 
        y=randint(1,6)

        sense.set_pixel(x,y,0,0,0) #set colour of random pixel to 0,0,0 to clear
        count +=1
        sleep(0.005) #faster pixels
