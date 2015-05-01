from random import randint

dice_outcome = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
roll_store =[]

for key in range(500):
  save = randint(1,6) + randint(1,6)
  
