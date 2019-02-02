#total karo 21 se 421 tak
i = 12
j = 0
while i <= 421:
    j = j+i
    i=i+1
print j

"""Ek flowchart banao jo 30 se 420 tak unn numbers ka sum calculate kare jo 8 ke multiple hai yaani wo numbers 8 ke table (paahade) mein aate hai."""
a = 30
b = 0
while a <= 420:
    if a % 8 == 0:# this will chk weateher the number is divisible by 8
        b=b+a # this will total only the nubmers which are divisible by 8
    a=a+1 # increases the value
print b

"""Ek flowchart banao jo 11 logon ka weight input le aur fir average weight print kare. Aur firr yeh bhi check kare ki kya Average weight 5 ka multiple(yaani 5 se bhaag karne par shesh 0 bachta hai) hai ya nahi?"""
i = 0
total = 0
while i <=11:#condition is given
   weight = input("enter your weight:")# this will take the weights for 11 time beacuse of the condition given
   total = total + weight# this will total the weight
   i=i+1#A increment is done
print total
average = total/11#  this will remove the average of the weight
print average
if average % 5 == 0:#thid will chk weather the average is divisible by 5 or not
    print ("average is divisible by 5")
else:
    print ("not divisible")




        

