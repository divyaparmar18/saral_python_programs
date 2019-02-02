import random
def getSecretNum(numDigits):
# Returns a string that is numDigits long, made up of unique random digits.
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(numDigits):
    secretNum = secretNum + str(numbers[i])
  return secretNum



def getClues(guess, secretNum):
# Returns a string with the pico, fermi, None clues to the user.
  if guess == secretNum:
    return 'You got it!'
  clue = []
  for i in range(len(guess)):
    #print guess[i],secretNum[i]
    if guess[i] == secretNum[i]:
      clue.append("fermi")
    elif guess[i] in secretNum :
      clue.append("pico")
  if len(clue) == 0:
    return None
  return ' '.join(clue)

def playAgain():
# This function returns True if the player wants to play again, otherwise it returns False.
    play = raw_input("Do you want to play again? Yes or No?") 
    if play == "yes":
     return playAgain
    

def isOnlyDigits(num):
# Returns True if num is a string made up only of digits. Otherwise returns False.
  if num == '':
    return False

  for i in num:
    if i  in ["0","1","2","3","4","5","6","7","8","9"]:
      return True

print  isOnlyDigits("23468")



numDigits = 3
MAXGUESS = 10

print('I am thinking of a %s-digit number. Try to guess what it is.' % (numDigits))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  None       No digit is correct.')

while True:
  secretNum = str(getSecretNum(numDigits))
  print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
  numGuesses = 1
  while numGuesses <= MAXGUESS:
      #print 'Guess' + str(numGuesses)
      guess = raw_input("Guess Again")
      if len(guess) != numDigits or not isOnlyDigits(guess):
        print "not valid"
      clue = getClues(guess, secretNum)
      print(clue)
      numGuesses = numGuesses+ 1
      if guess == secretNum:
        break
      if numGuesses > MAXGUESS:
        print 'You ran out of guesses. The answer was ' +  str(secretNum)
        break
  if  not playAgain():
    break
    
         
