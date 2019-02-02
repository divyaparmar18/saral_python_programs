"""Ab aap ek program likhoge jo ki user se ek integer input lega aur fir uska factorial print karega. Agar user 3 dalega to 6 print karega, 7 dalega toh 5040 print karega aur aise hi dusre numbers ke lie."""
number = input("enter a number")
i=1# here we assign i as 1
j=1#here  we took one more variable as j and gave the value 1
while i <= number:# here we gave the condition to run the loop till the number given by user
    j=j*i# here we gave the value to the j that whatever the result of j and i multiplication will be the value of j as we have to remove the factorial so we have to multiply
    i=i+1# here we did the incremetn of i so that it could reach the nubmer and stop the loop and also i will keep on getting multiplied by j
print j# finally we print the result our j