#here we will take the input from the user and we will see how to work with strings ,integers and floats
name = raw_input("put your name: ")
surname = raw_input("put your surname: ")
whole_name = (name  +  surname)
print (whole_name)#this will add the string and print both the srting to gether bcoz raw input means that user will input sometihng in string form
first = input("enter a number")
second = input("enter another number")
third = (first+second)
print (third)#this will add both the nubmers bcoz we took the input that means in a integer or floatr form
fourth = raw_input("enter a float")
fifth = raw_input("enyter another float")
sixth = (fourth+fifth)
print (sixth)#this will print both the floats together bcoz the input is taken in as a raw input which means that it is in strijng format
#so now we will convert the raw_input which is in string form in a integer
seventh = int(fourth)
eight = int(fifth)
nine = (seventh+eight)
print (nine)#here we have converted the raw_input to integer so now they will add the numbers