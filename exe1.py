"""1 se 1000 tak saare numbers print karne ka loop likho. Lekin
Agar number 3 se divisible hai toh "nav" print karvao.
Agar number 7 se divisible hai toh "gurukul" print karvao.
Agar number 21 se divisible hai toh "navgurukul" print karvao."""
 
i = 0# here i initialise the value of i
while i < 1000: #here i give the condition that the loop should run till i is less thn 1000
    if i % 21 == 0: #here i give the condition that if i is divided by 21
        print "navgurukul" #so if the upper condition is true thn  instead if i it will print navgurukul
    elif i % 7 == 0: ##here i give the condition that if i is divided by 7
        print "gurukul" #so if the upper condition is true thn  instead if i it will print gurukul
    elif i % 3 == 0: #here i give the condition that if i is divided by 3
        print "nav" #so if the upper condition is true thn  instead if i it will print nav
    else:# so if all the upper conditions are not true loop comes here
        print i# and i will get printed
    i=i+1 #here we did the increment of i so it will keep in increasing
     
