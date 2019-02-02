#add_numbers naam ka function likhiye jo do numbers ko arguments ke tarah le aur fir unka sum print karta hai. Arguments ka naam number1 aur number2 hona chaiye.

def add_numbers(number_1,number_2):# here i made a function
    print number_1 + number_2# in the function i asked to print the sum of the parameters which will be given in the function

add_numbers(23,44)# here i called the function with giving the parameters
add_numbers(10,30)# here i called the function with giving the parameters


#add_numbers_list naam ka function likhiye jo do integers ki 2 lists leta ho aur fir same position wale integers ka sum print karta ho.

def add_numbers_list(list_1,list_2):# here i made a function which has two list as parameters
    i=0# i assign a variable which will tell the place of the element of the number in the list 
    while i < len(list_1):#here we gave the condition to run the loop till i is lless thn the length of the list
        print list_1[i] + list_2[i]#this will print sum of the first numbers of the list as the i is 0 so the elements at 0 place will get added to eachother
        print "----------------"#this will print as it is
        i=i+1#here we do the increment so thew i will increase and also the loop will run further and add other elements as the place will chng

add_numbers_list([12,40,30],[10,55,60])# here we called the function and also gave two lists as parameters