#now we will make a kbc game over here in pytohn and write the code
question = ["which one is software","what is set of instruction called","which is a programming language","which is a framework","which code is a machine code"]
first_option = ["mouse","server","english","django","source code"]
second_option = ["application","client","hindi","java","diff code"]
third_option = ["keyboard","data","pytohn","java.script","sudo code"]
fourth_option = ["monitor","variable","spanish","c++","object_code"]
all_option = [first_option,second_option,third_option,fourth_option]
print question[0]
print first_option[0]
print second_option[0]
print third_option[0]
print fourth_option[0]
print all_option[0][2]
print all_option[1][2]
print all_option [2][2]
print all_option[3][2]
question.pop()# this will remove the last element of the list
first_option.pop()
second_option.pop()
third_option.pop()
fourth_option.pop()
print len(question)
question.append("What do we need to connect with another laptop far away")# this will add the element in the list
first_option.append("usb")
second_option.append("remote")
third_option.append("computer")
fourth_option.append("internet")
option2 = second_option[1]
print option2
if option2 in third_option:# this will chk weather the option2 is there in third_option
    print "yes"
else:
    print "not"

question = ["which one is software","what is set of instruction called","which is a programming language","which is a framework","which code is a machine code","what is needed to connect to server","which is operating system","what is brain of computer","which one is hardware","what is assignment to a value called"]
first_option = ["mouse","server","english","django","source code","internet","data","keyboard","apps","variable"]
second_option = ["application","client","hindi","java","diff code","usb","software","speaker","program","boolean"]
third_option = ["keyboard","data","pytohn","java.script","sudo code","remote","linux","monitor","laptop","operators"]
fourth_option = ["monitor","variable","spanish","c++","object_code","program","monitor","CPU","python","function"]
all_option = [first_option,second_option,third_option,fourth_option]
answer_key = [1,2,2,0,3,0,2,3,2,0]