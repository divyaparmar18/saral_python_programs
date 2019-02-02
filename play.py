def playAgain():
# This function returns True if the player wants to play again, otherwise it returns False.
    play = raw_input("Do you want to play again? Yes or No?") 
    if play == "yes":
        return play.lower() 
    
print playAgain()