from gopigo import #import all function from the gopigo library
import time #allows you the time.sleep() function
import math #allows you to use math functions like floor()

set_speed(100) #you can use values from 0 to 225

def move_forward(feet): #make a function that takes in a number of feet and moves the robot foward that far 
  mm = feet * 304.8
  steps = mm/11.338
  enc_tgt(1,1,steps)
  time.sleep(.1) #can make mtor movement more reliable 
  fwd() #motion function in the gopigo library
  time.sleep(feet*2) #set this wait for as long as the movement will take 
  
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
move_foward(4)
turn_right
move_foward(3)
turn_right
move_foward(3)
turn_left
move_foward(2)
turn_left
move_foward(4)
