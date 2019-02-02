string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
new_list = []# here we made a new list so that uniq elements will be added in this
for i in string_list:# here we used for loop so say that as all elemnets of the list to be taken
    if i not in new_list:# we gave condition if any element of string list is not in new list
        new_list.append(i)# then it should be added in this list
print new_list# here we get the new list with all uniq elements