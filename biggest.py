#raw_input ka use kar ke 3 alag variables mein 3 integers ka input lein. Input lene ke baad inn 3 mein se sabse bade number ko print karo

first = raw_input("enter a number")# we took a input from a user in a string form
First = int(first)#we converted string into integer
second = raw_input("enter another number")# we took a input from a user in a string form
Second = int(second)#we converted string into integer
third = raw_input("enter one more number")# we took a input from a user in a string form
Third = int(third)#we converted string into integer
if First > Second and First > Third:# here we gave the condition that if first number is greater thn second and third
    print First# then first nubmer will be printed
elif Second > First and Second > Third:# here we gave the con dition that if second nubmer is greater thn first and third
    print Second# thn second nubmer will be printed
else:# if all the upper conditions are not true 
    print Third# then thisd will be printed