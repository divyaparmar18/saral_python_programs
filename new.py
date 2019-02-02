list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
list3 = []# here we took a empty list
for i in list1:# here we use the for loop and take all the elements
    if i not in list3:#here we chk that if element is not in list3
            list3.append(i)#we tell the computer to add that element in the list
for i in list2:# here we use the for loop to take all the elements of thelist
    if i not in list3:# we chk weather that element is there in the lsit or no
        list3.append(i)# if not that add that element in the list3
print list3Z# here we print the new list