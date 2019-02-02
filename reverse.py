#Code likho jo neeche di gayi lists ke items ko reverse order yaani ki ulta print kare.

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
place = list(reversed(places))#this is a biult in function in python toi reverse any list or string or anythin else
print place

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]#here we will reverse the list by loop
i=0 # so here we assign the index as 0
new_list = [] # here we assigned a empty list
length = len(places) # this will remove the length
while length>0: # here we give the condition to run the loop
    new_list.append(places[length-1]) # this will add  the last element of the list and then keep on printing it  with the loop
    length=length-1 # here we are going on with the decrement
print new_list # this will print the reversed form of earlier list

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] # here we will print all the elements of the list in vertically
i=0 # here we assign index as 0
while i < len(places): # here we give the condition to run the loop to till the length
    print places[i] # this will print the first element of the list
    i=i+1 # here we give the increment

