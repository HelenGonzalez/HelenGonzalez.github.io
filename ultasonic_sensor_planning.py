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

while (1 > 0):
  if us_dist(15) > 10;
    fwd()
  else:
    stop()
    servo(0)
    left = us_dist(15)
    servo(180)
    right = us_dist(15)
    if right > left:
      turn_right()
    else:
      turn_left()
    servo(90)
