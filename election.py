from random import random

for i in range(10000):
  regions = 0
  if random.random(100) <= 87:
    regions +=1
    if random.random(100) <= 65:
      regions += 1
    if random.random(100) <= 17:
      regions += 1
  if region >= 2:
    print "Candidate A wins!"
  else:
    print "Candidate B wins!"
    
