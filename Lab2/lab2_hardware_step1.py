from sense_hat import SenseHat
import time
from time import sleep

sense = SenseHat()

# colours
yellow = (255, 255, 0)
green = (0, 255, 0)

#display loop
sense.clear()
#count value to help iterate between the two letters.
#if even: N, if odd: F
count = 0; 


while True:
  for event in sense.stick.get_events():
    # if joystick was pressed
    if event.action == "pressed":
      
      # if any direction
      if event.direction == "up" or "down" or "left" or "right":
        #if even show N
        if count % 2 == 0:
          sense.show_letter("N", yellow)      
          time.sleep(0.5)
          count+=1
        #if odd show F
        else:
          sense.show_letter("F", green)      
          time.sleep(0.5)
          count+=1
        
      # Wait a while and then clear the screen
      sleep(0.5)
      sense.clear()
          
