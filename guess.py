#guessing game with 5 chances
num = 5 #here we took a number  which will be the number taken by the computer and the user has to guess this number 
i=0# here we initialize i as 0 to run our loop
while i < 5:#here we gave the condition to run nthe loop till i is less thn 0
    number = input("enter a nubmer between 0 to 10 : ")# here user will guess the nubmer and inupt one nubmer
    if number > 10:#here if the user guesses the number above 10 here we gave the condition if
        print ("out of range")# if upper condition true thn it will print out of range
        break# and the game will break
    elif num == number:# here we will chk weather the number guessed by the user is equal to the number guessed by the computer
        print "you won"# if the upper conditiom is true then this will gewt printed the user has won the game
        break# becoz of the the game will stop
    else:#if upper condition is not true thn it comes here
        i=i+1# and increment is done
if num != number:# if number is not equal condition is given
    print "you lost"# # if numbers are not equal to number then this will be printed