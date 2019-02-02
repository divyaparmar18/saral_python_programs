# here we will see how to work with files in python

my_file = open("people1.txt")# here we open a file with this command
file_data = my_file.read()# then by writing .read we can read the file
print file_data# this will print the data so that we can read the file
my_file.close()# we have to always close the file

my_file2 = open("people2.txt","w")# here we made a file by writing open and "w" which means to write 
my_file2.write("Abhishek - Gurgaon \n")# here by .write we can write whtever we have to write
my_file2.write("Ranveer - Delhi")# here we write the second thing wht we hacve to write
my_file2.close()# close the file 

print "AbhishekRanveer"
print "---------------------------------"
print "Abhishek\nRanveer"
print "---------------------------------"
print "Abhishek\n\nRanveer"
print "---------------------------------"

my_file3 = open("people3.txt","w")# made a new file
my_file3.write("Abhishek - Gurgaon \n Ranveer - Delhi")# wrote this in the file with \n so that pytohn goes on nxt line
my_file3.close()# close the file

my_file4 = open("test_file.txt","w")# made a file
my_file4.write("yaha main kuch likha")#wrtoe txt
my_file4.write("\n yaha maine kuch aur bhi likha")
my_file4.close()# closed the file
#my_file4.write("aur kuch likhna hai") this wont work because the file is closed

batch1_students = ["Shivam","Rahul","Kavya","Dhannu","Deepanshu","Nitin","Manoj","Shakrudin","tara","Suraj","Krishna"]# here we gave a list
students_file = open("NavGurukul Students","w")# made a new html file
students_file.write("<html>\n")# wrote the contents of the html file one by one
students_file.write("<head>\n")
students_file.write("<title> NavGurukul Students </title>\n")# gave the title
students_file.write("</head>\n")
students_file.write("<body>\n")
students_file.write("<ul>\n")
for students in batch1_students:# here we gave the for loop to be ran in the list
    students_file.write("<li>" + students + "</li>\n")# here all the contents of the list will be printed
students_file.write("</ul>\n")
students_file.write("</body>\n")
students_file.write("</html>\n")
students_file.close()# here we closed the file

my_file = open("people1-exercise.txt","w\n")# made a file 
my_file.write("rishabh - meerut\n")# wrote all the lines
my_file.write("imtiyaz - delhi\n""nilima - cochin\n""rati - shimla\n""ayishah - delhi\n""raghu - shimla\n")
my_file.write("neela - delhi\n")
my_file.write("sashi - jaipur\n")
my_file.write("naseer - kanpur\n""karthikeyan - delhi\n""salma - jaipur\n""pankaj - delhi\n")
my_file.write("brijesh - delhi\n")
my_file.write("govind - delhi\n")
my_file.write("puneet - shimla\n")
my_file.write("siddhi - delhi\n")
my_file.write("suman - jaipur\n")
my_file.write("rajeev - shimla\n")
my_file.write("mohinder - delhi\n")
my_file.write("rajendra - jaipur\n")
my_file.write("priyanka - shimla\n")
my_file.write("sarika - delhi\n")
my_file.write("deepti - shimla\n")
my_file.write("harshad - delhi\n""trishna - raipur\n")
my_file.write("pradeep - jaipur\n""sekhar - delhi\n""nand - delhi\n""anoop - delhi\n""balwinder - tokyo\n")
my_file.close()# closed the file

my_file = open("people1-exercise.txt")#made a file
my_data = my_file.read()# took a variable  and stored it to read the file
for lines in my_data:# we ran the loop in the data of the file
    num = my_data.count("\n")# we count the number of "\n in the data"
print num# this will print the num of \n

file_name = ("people1-exercise.txt")# here we made a file
num_lines = 0# took vaiable for the num of lines
with open(file_name,"r") as f:# here we opened the file and declared the data as f
    for lines in f:# here we ran the loop in the data
        num_lines = num_lines + 1# this will count the number one by one of the lines
print num_lines# this will print the nubmer of lines

my_file = open("people1-exercise.txt")# opened the file
my_data = my_file.read()# took a variable and read the file
num_lines = 0# took a variable  n gavevalue 0
for lines in my_data:# here we ran a for loop in the file
    num_lines = num_lines+1# it goes on adding the words in the file
print num_lines# this will print the words

banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]# took a list
new_file = open("question3.txt","w")# made a file and opened it to write
for strings in banks_list:# ran a loop in the list
    new_file.write(strings + "\n")# this will write the elements of the list in this file
new_file.close()# close file

file_name = open("people1-exercise.txt")# opened a file from which strings has to be taken
my_file = open("Delhi.txt","w")# made a new file
new_file = open("Shimla.txt","w")#made a new file
other_file = open("Others.txt","w")#made a new file
for lines in file_name:# ran for loop in the first file from which we have to access data
    if "delhi" in lines:# so if delhi is there in the line of the file
        my_file.write(lines)# that line will be written in the file
    elif "shimla" in lines:# so if delhi is there in the line of the file
        new_file.write(lines)# that line will be written in this file
    else:# if upper condition not true the loop comes here
        other_file.write(lines)#the data will be written in this file
   
my_file.close()
new_file.close()
other_file.close()
file_name.close()# all files will be closed