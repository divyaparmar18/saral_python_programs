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

print getClues("345","456")