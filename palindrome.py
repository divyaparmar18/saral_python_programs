

name = ['n','i','t','i','n']
names = list(reversed(name))#this is a reversed function in python which reverses the list
if name == names:# it chks weather both the list are similar or not
    print "its a palindrome"#if condition true it prints this
else:#if upper condition not true comes here
    print "its not a palindrome"# then this is printed

name = ['n','i','t','i','n']
i = 0# here we took the index as 0 as it stars from 0, index is the places of the elements of the list so first element is a 0 place
reverse_list = []# here we took a empty list
length = len(name)# there is a buildin function in python called len which calculates the length of the list
while i < length:#here we give the condition that loop should run till i is less thn length of list
     reverse_list.append(name[length-1])#here we appended the last element of the list by indexing it as length - 1 in the reverse_list
     length=length-1#here there is decrement of the length of the list as in upper line the indexing will get less and it will go on appending the elements in reverse form
print reverse_list# this will print the reverse_list with the elements appended in it
if name == reverse_list:#this will chk weather the normal and reverse list are similar or not which means palindrome or not
    print "its a palindrom"#if condition true prints this
else:#if upper condition not true
    print "its not a palindrome"#prints this

name = raw_input("enter a list of names of character")#here we take raw_input from the user
name = list(name)#we convert that string into list  to chk weather it is a palindrome or not
i=0# here we took the index as 0 as it stars from 0, index is the places of the elements of the list so first element is a 0 place
new_list = []# here we took a empty list
length = len(name)# there is a buildin function in python called len which calculates the length of the list
while i < length:#here we give the condition that loop should run till i is less thn length of list
    new_list.append(name[length-1])#here we appended the last element of the list by indexing it as length - 1 in the reverse_list
    length=length-1#here there is decrement of the length of the list as in upper line the indexing will get less and it will go on appending the elements in reverse form
print name#this will print the list by user
print new_list# this will pritn the reverse list which we got after this code
if name == new_list:#trhis will check weather both list are similar or not
    print "Its a palindrome"# if they are similar this will print
else:#if upper condition not true this will print
    print "Its not a palindrome"#this will print


