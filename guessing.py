#guessing game with 10 chances

num = 8 #here we took a number  which will be the number taken by the computer and the user has to guess this number 
i=0 #here we initialize i as 0 to run our loop
while i < 10: #here we gave the condition to run nthe loop till i is less thn 0
    number = input("enter a nubmer between 0 to 10 : "# here user will guess the nubmer and inupt one nubmer
    if number > 10: ##here if the user guesses the number above 10 here we gave the condition 
        print ("out of range")# if upper condition true thn it will print out of range
        break# and the game will break
    elif num == number:# here we will chk weather the number guessed by the user is equal to the number guessed by the computer
        print "you won" # if the upper conditiom is true then this will gewt printed the user has won the game
        break #becoz of the the game will stop
    elif num < number: #here we give the condition that if the number nubmer is less thn number 
        print "you number is greater thn my number" #if upper condition is true then this will be printed
    elif num > number:# here we give the condition that if the number is less thn num thn 
        print "your number is lesser thn my nubmer"# this will tell the user that his nubmer is less thn the computers number
    i=i+1 # here we do the increment
if num != number:# here we give the condition that if the number is not equal to the computers nubmer
    print "you lost"# the user is not ablwe to guess the number and will tell u lost the game