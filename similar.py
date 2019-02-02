list1 = [1, 342, 75, 23, 98,44]
list2 = [75, 23, 98, 12, 78, 10, 1,44]
list3 = []# here we took a empty list 
for i in list1:# here we take all the elements of list1
    for i in list2: # here we take all the elements of list2
        if i in list1 and i in list2:# so here we give the condition that if the element is there in both the list
            if i not in list3:# if that element is not in the list3
                list3.append(i)#thn those elements should be added in the list3
print list3# new list will be printed