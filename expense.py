#Iss program mein hum students ki ginti aur ek student ke kharche se hisaab se pure NavGurukul ka ek mahine ka kharcha nikalenge

num_of_student = input("enter the number of students") #here wqe take the nubmer of students from user
expense_student = input("enter the expense of each student")# here we take the expense of each student
total_expense = num_of_student*expense_student# here we calculate the total expense
if total_expense <= 50000:# here we gave the condition that if the total expense of students is less thn 50000
    print "We are in budget"# then they are in budget
else:# if upper condition is not true thn loops comes here
    print "we are not in budget"# this will get printed that we are not in budget