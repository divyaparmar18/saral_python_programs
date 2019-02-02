#writwe a code in a loop to print 0 to 10 numbers
i = 0 # here we assigned the value to i as 0 so our loop will start from 0
while i <= 10: # here we give the condition that till where the loop should run
    print i # here we print our result
    i=i+1 # this is the iteration that the value of the variable will increase by 1
#Aapko 11 aur 45 bhi print karna hai.

a = 11
while a <= 45:#condition is given to run the loop till a is 45
    print a#print the number
    a=a+1#increases the number one by one

"""Ek buiding hai jisme 10 floors hai. Aur aap uss building ke ground floor par ho. Aapko uss building ke top floor par jaana hai. Aap ek baar mein ek floor hi chadh sakte ho. Ground floor se top floor per jaane ka flowchart banao. Jab aap top par phonch jayenge tab aapko "mein top par pahunch gaya"print karna hai."""

floor = 0
while floor <= 10:#gave the condition to run the loop till floor is eqaul to 10
    print ("aap abhi " + str(floor) + " floor pr pahoche" )
    if floor == 10:#conditrion is given
        print ("aap sabse top floor pr pahoch gaye ho")# this gets printed
    floor = floor + 1# increment ius done

"""Ek code likho jo 20 se 100 mein wahi numbers print kare jo 2 se divisible hai yaani numbers ka 2 se bhaag karne par remainder (shesh) 0 bachta hai."""
i = 20
while i <= 100:#gave the condition to run the loop till floor is eqaul to 100
    if i % 2 == 0:#condition is given
        print i#prints the number
    i=i+1# increment is done

#Ek code likho jo 1 se 100 mein wahi numbers print kare jo 7 se divisible hai yaani unka 7 se bhaag karne per remainder (shesh) 0 bachta hai.
i=0
while i <= 100:#gave the condition to run the loop till floor is eqaul to 100
    if i % 7 == 0:#condition is given
        print i#prints the number
    i=i+1#increases the number

#Ek flowchart banao jo 30 se 400 tak aise numbers print kare jo 3 aur 21 dono se divisible hai.

a = 30
while a <= 400:#gave the condition to run the loop till floor is eqaul to 100
    if a % 3 == 0 and a % 21 == 0:#condition is given
        print a#prints the number
    a=a+1# increment is done

