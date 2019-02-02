# here we are making a function which will take list of students marks and print their highest marks

def max_num(list_of_marks):# here we made a function of name max_num
    index = 0# here we declared the index of the list as 0
    while index < len(list_of_marks):# here we give the condition to run the loop till the index is less thn lenght of the list
        print max(list_of_marks[index])# this will remove the max number from the list as max is the inbuit function in pytohn
        index=index+1# here we did the increment of the index

max_num([[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]])# here we called the function with a list in list parameter
