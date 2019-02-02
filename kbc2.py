#now we will make a kbc game over here in pytohn and write the code
question = ["which one is software","what is set of instruction called","which is a programming language","which is a framework","which code is a machine code"]
first_option = ["mouse","server","english","django","source code"]
second_option = ["application","client","hindi","java","diff code"]
third_option = ["keyboard","data","pytohn","java.script","sudo code"]
fourth_option = ["monitor","variable","spanish","c++","object_code"]
all_option = [first_option,second_option,third_option,fourth_option]
answer_key = [1,2,2,0,3]
length = len(question)
i=0
answer_list = []
while i < length:
    print ("* " +question[i] + "? - " + str(len(question[i])))
    k=0
    while k < len(all_option):
        print (str(k) + "." + all_option[k][i] )
        k=k+1
    user = input("enter a number from 0 to 4:-")
    if user > 5:
        i = i-1
        print "not valid"
    if user < 5:
        answer_list.append(user)
        if user == answer_key[i]:
            print "your answer is correct"
        else:
            print "Sadly, your answer is incorrect"
            print "you lost the game better luck next time"
            break
    i=i+1