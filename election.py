from random import randint
win=0
for i in range(10000):
  regions = 0
  if random(1,100) <= 87:
    regions +=1 #adds to region
    if randint(1,100) <= 65:
      regions += 1
    if randint(100) <= 17:
      regions += 1
  if region >= 2:
    win += 1 #adds to wins 

print "Candidate A would have won the elections %s percent." %(win/range(10000))
