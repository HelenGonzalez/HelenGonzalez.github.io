from gopigo import *
import time

def turn_right():
  enc_tgt(1,0,14)
  time.sleep(.1)
  right()
  time.sleep(2)
  
def turn_left():
  enc_tgt(0,1,14)
  time.sleep(.1)
  left()
  time.sleep(2)
  
servo(90)

while (1 > 0): #forever loop
  if us_dist(15) > 10;
    fwd()
  else:
    stop()
    servo(0)
    left = us_dist(15) #save the distance of the left side
    servo(180)
    right = us_dist(15) #save the distance of the right side
    if right > left: #compares the distance of anobject close to it
      turn_right()
    else:
      turn_left()
    servo(90) #turns the servo foward
