from random import randint
user = raw_input("enter ")
moves = ["rock","paper","siccssor"]
comp = randint(0,2)
computer = moves[comp]
print computer
if comp == user:
    print "you won"
else:
    print "you lost"