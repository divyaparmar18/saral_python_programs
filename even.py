#take a chk_num function and cvhk the arguments are3 even or not
def check_numbers(num_1,num_2):#here i made a function with two parameters to be taken
    if num_1 % 2 == 0 and num_2 % 2 == 0:#this is the condition 
        print "both numbers are even"#if condition true this will print
    else:#if upper condition not true it comes here
        print "Both numbers are not even"#this gets printed

check_numbers(22,34)#here we call the function

#Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list ko arguments ki tarah le aur fir check kare ki same index waale dono integers even hain ya nahi.

def check_numbers_list(list_1,list_2):#here i made a function with two parameters to be taken
q   i=0 #assigned a variable for the index of the list
    while i < len(list_1):#gives the condition to the loop to run till i is eqaual to the length of the list
        if list_1[i] % 2 == 0 and list_2[i] % 2 == 0:# this will chk weather indexting elements of both hthe list are even or not
           print "Both numbers are even"#if condition true it gets printed
           print "-----------------"
        else:#if upper condition not true it comes here
            print "Both numbers are not even"#this gets printed
            print "-------------------"
        i=i+1# here we do the increment so that index keep on inrceasing

check_numbers_list([23,32,12,45,20],[21,34,23,43,10])# here we call the function and also gave the two listsa as parameters