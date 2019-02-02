#Ek flowchart banao jo fibonacci series ke pehle 100 number print kare. Fibonacci series aisi hoti hai:
a = 0
b = 1
c = a + b
print a# this will print it
print b # this will print it
while c < 100: # thid will chk the condition weather the c which means sum of a and b is less thn 100
    c = a + b # here we wrote that c will be a + b so the value of first and second number will be added
    a = b # here we chnged the value of a to b
    b = c # here we chnged the value of b to c
    if c < 100:# here we chk weather c is still lesser thn 100
        print c
""" so in fibonacci series we print the first and second number then we assign a variable where we add the first two numbers then we chng the values of first vaiable to second and second to third so the flow goes on adding and chnging the vlaues to get the addition of the number of result we are getting"""
    