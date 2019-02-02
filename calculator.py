"""calculator naam ka ek function banao jo teen argument leta ho - number_x, number_y, operation. number_x aur number_y mein hum humesha do integers denge aur operation mein kaunsa operation karna hai woh denge."""
def calculator(number_x,number_y,operator):# here we amde a function which has three arguments
    if operator == "add":# here is the condition weather the operator is "add"
        sum = number_x + number_y# here if the upper condition is true then the numbers in the parameters should add with each other and we have given a variable also to it
        return sum# here the result of sum will be given
    elif operator == "subract":# as earlier we gave the conditionn of adding here we givwe the condition of subracting
        sub =  number_x - number_y# so if the condition is true then the numbers in the parameter will subract
        return sub# this will return the result after subracting
    elif operator == "multiply":# here we give the condition of multiplication that weather the operator is multiply
        mul =  number_x * number_y# here also we take a variable to store the result as we did earlier and then if the condition is true then it will multiply the numbers in the parameters
        return mul# this will return the result after the multiplication
    elif operator == "divide":# here same as we didi earlier we gave the condition weather the operator is divide
        div = number_x / number_y# here also we gave a new variable to the result after the condition is true it will divide the numberss and store the reult in the new variable
        return div# this will return nthe result of the division 
   

Addition = calculator(10,30,"add")# here we took the variable and called the calculator function and also gave the 3 arguments/parameters
print Addition# here we have to print this variable because earlier we were printing in the function so it was only needed to call but as it returns value we have to print the variable in which function is called
Subraction = calculator(25,6,"subract")#same we are doing this only one parameter which needed the operator is different
print Subraction#this will print the result after using the upper parameters in the calculator function
Multiplication = calculator(25,5,"multiply")# this is also same in this one parameter is multiply and this will multiply the integers
print Multiplication# this will print thhe result by using upper parameters in the calculator function
Division = calculator(600,10,"divide")#this is also the same jst one parameter is different
print Division#this will print the result taking the upper parameters in the calculator function

#Ab raw_input ka use kar ke user se 2 numbers input lo.Fir calculator function ko 4 baar call call kar ke inn dono numbers do add, subtract, multiply, divide karo aur result ko 4 alag variables mein daalo. Woh variables ka naam yeh hoga:

first_num = input("enter a number")# user will put one number as a first parameter
second_num = input("enter another number")# user will put another number as a second parameter
Add = calculator(first_num,second_num,"add")# this will take both the input and as calculator function is stored in Add variable it with one parameter add
print Add# so this will print the result after the calulator function is called with add operator
Sub = calculator(first_num,second_num,"subract")# so in the calculator code operator condition are given so if the operator is "subract it will subract the numbers given by user"
print Sub#print the result aafter calling the calculator function
Multiply = calculator(first_num,second_num,"multiply")#this will multiply both the numbers given by the user as the operator is "multiply" 
print Multiply#pritn the result of function after calling with the given parameters
Divide = calculator(first_num,second_num,"divide")# thsi will divide the the parameters given by the users
print Divide# print the result after calling the function


"""list_change naam ka ek function ka code likho jo 2 lists jisme integers arguments ki tarah le aur fir unn lists ki woh items jo same index number (kram) pe hain unko multiply kar ke ek nayi list return karvaye."""

def list_change(list_1,list_2):# we made a new function which takes two lists as parameters
    i=0# here we defined the index of the lists
    multiply_list = []#we took a new empty list 
    while i < len(list_1):#now we gave the condition that the loop should run till the index is smaller than the length of the list
        result = calculator(list_1[i],list_2[i],"multiply")# here we assign a new variable and in that variable we called the function calculator by taking the first numbers of both the list through i which indicates index and giving the operator to multiply
        multiply_list.append(result)#so now here we append the result after calling the function in the empty list as we want a new list of multiplication of indexed numbers of both lists
        i=i+1#here we do the increment where index will become one and the whole process will continue with 1 index thn go in inceasing
    return multiply_list # finally after the loop is finished we return the multiply_list which has the result if indexed multiplication of both list
    


final = list_change([2,3,10,5,8],[10,4,35,2,4])# here we took a variable name final and called the calculator function in it with is lists
print final# this will print aor result

