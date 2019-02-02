# here we will make a game in which we will fight with the alien 

from random import randint # allows you to generate a random number
# variables for the alien
alive = True
stamina = 10

# this function runs each time you attack the alien
def report(stamin):
    if stamin > 8:#here we give the condition 
        print "The alien is strong! It resists your pathetic attack!" # if upper condition is true this will be printed
    elif stamin > 5:# if upper condition is not true loop comes here to another condition
        print "With a loud grunt, the alien stands firm."# this gets printed if upper condition is true
    elif stamin > 3:# so if stamin is less thn 3 then condition will be true
        print "Your attack seems to be having an effect! The alien stumbles!"# and this will get printed
    elif stamin > 0:# here one more condition is given if upper all conditions are false, loop comes here
        print "The alien is certain to fall soon! It staggers and reels!"# and this gets printed
    else:# if above all conditions are false then loop comes to the else part
        print "That's it! The alien is finished!"# and this is printed

# main function - accepts your input for fight with the alien
def fight(stam): # stamina
    while stam > 0:# here condition is given if stam to run the loop till stam is greater thn 0
      # won't enter this loop ever. The function will always return False.
        response = raw_input("> Enter a move 1.Hit 2.attack 3.fight 4.run")# here give a option to user to choose
        # chose a response from ( hit, attack, fight and run)
        # fight scene
        if "hit" in response or "attack" in response:# here we give the condition
            less = randint(0, stam)# if upper condition is true by using builtin function computer choses a number between 0 and stam
            stam = stam - less # subtract random int from stamina
            report(stam) # see function above
        elif "fight" in response:# if user choses to fight
            print "Fight how? You have no weapons, silly space traveler!"# this will be printed
        elif "run" in response:# if user choses run 
            print "Sadly, there is nowhere to run.",# then this will be printed
            print "The spaceship is not very big."
        else:# if upper all the conditions are not true loop comes here
            print "The alien zaps you with its powerful ray gun!"# this gets printed
            return True# and it returns true
    return False

print "A threatening alien wants to fight you!\n"
# quotes at the end.

# call the function - what it returns will be the value of alive
alive = fight(stamina)

if alive: # means if alive == True
    print "\nThe alien lives on, and you, sadly, do not.\n"
else:
    print "\nThe alien has been vanquished. Good work!\n"
