"""def find_in_list(query, mainlist):
# this function is used to find the position of the "query" in the "mainlist". If "query" is in the list then it returns its position, otherwise it returns None
    mainlist_len = len(query)
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = mainlist[i]
        if element == query:
            index = i
    return i
# this should return the position of the "query" in the "mainlist"""


def find_in_list(query,main_list):#here we made a function with two arguments to be taken one a query and a main_list to chk weather the query is in main_list or no
    length = len(main_list)# as in the upper function main_list length was declared as length of query but query length and main_list length is big so it cant be equal so to run the loop in whole list we used len method and declared the length of the main_list
    range_for_loop = range(length)#here we gave the range till where the loop has to run till the length of the main_list
    index = None # here we declared the index as none as we have to find in quesry is in list thn we have to remove the index or else it will remain none only
    for i in range_for_loop:# here we used for loop to run through the range ehich is till the length of the main_list
        if query == main_list[i] :# so here we will chk that if any element is equal to query or not so if it is equal
            index = i # index will become the index of the element in the list
    return index # this will return the index
    

check = find_in_list("Pratik",["Pratik","Danny","Popi","zoyaa"])# here we took a variable named chk and we called the find_in_list function by giving the two arguments
print check# here we printed the check variable which will give the output ogf the function 