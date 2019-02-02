from random import randint# here we import the library name random from randint that lets the computer to intake a random number

def win():here we made a function named win
    print 'You win!'# so whn this function will be called it will print you win

def lose():# here we made a another function 
    print 'You lose!'# so whn this function will be called it will print you loose

while True:# here we give the condition that while true the code will run forward
    player_choice = raw_input('What do you pick? (rock, paper, scissors)')# here we take a raw input from the user and tell him to select any one from rock, paper and scissor
    
    random_move = randint(0, 2)# here as we imported random here we ask the computer to select any random number from 0 to 2
    moves = ['rock', 'paper', 'scissors']# here we made the list of moves which we will use further
    computer_choice = moves[random_move]# so now we use the list and see that the number selected by the computer will be the index of the list so through the index we come to know that which word from the list has been taken by computer
    print computer_choice# here it prints wht computer has choosed
    print player_choice# here the users input will be printed

    if player_choice == computer_choice:# here we give the condition that if user choice and computer is equal
        print 'Draw!'#it will print draw
    elif  player_choice == 'rock' and computer_choice == 'scissors':# here we give the condition
        win()# if upper condition is true this function will be called
    elif player_choice == 'paper' and computer_choice == 'scissors':# here we gave the condition
        lose()# if uppercondition is true this function will be called 
    elif player_choice == 'scissors' and computer_choice == 'paper':# here we gave the condition 
        win()# if the upper contion is true this function is called
    elif player_choice == 'scissors' and computer_choice == 'rock':# here we gaVe the condition
        lose()# if upper condition is true then this function is called
    elif player_choice == 'paper' and computer_choice == 'rock':# here we gave the condition 
        lose()# if upper condition is true then this function is called
    elif player_choice == 'rock'  and computer_choice == 'paper':# here we give the condition
        win()# if the upper condition is true thn this function is called
    again = raw_input('Do you want to play again? (y or n)').strip()# here we take a raw inpupt from the user to to ask weather he wants to continue the game or no
    if again == 'n':# here we give the condition that if user says no thn
        break# the game will break with this break condition and if the user enters y thn the game continues as up over there while ture condition is given and while true means true condition