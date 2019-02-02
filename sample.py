numbers = raw_input("enter a nubmer")# here we took a raw input which will be in string form from the user
num = int(numbers)# here we took a variable and chnged the type of the input bcoz we will need it further
number_list = list(str(numbers))# here as we took a string so we converted it into a list so that all the numbers will get seperated
i=0#here we initialize the index of the list to run the loop inside the list
j=0#here we took the variable j to store the sum of numbers in the list
while i < len(number_list):# here we gave the condition to run the loop till index is smaller thn the length of the list
  j=j+int(number_list[i])# here we did increment of the j by adding the elements of the list one by one and also we converted the elements from mstring to integer
  i=i+1# here we did the increment of the index of the list
print j# we printed the total of the elements of the list in a integer
if num % j == 0:# so here now we chk that the number user input is divided by its own sum or not
    print "harshad number hai"# if the condition is true and it is divided by its own thn this will print
else:# if upper condition is not true
    print "harshad nubmer nahi hai"# this will print
