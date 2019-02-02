# now in this file we are writing a code to encrypt or decrypt a msg so here we have two list in which all characters are wqritten and in second list we ahve written the characters as they had to be shifted by 2 so a will become c

chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

def find_in_list(query,main_list):# now here we make the first function named find in list which we will use further 
    length = len(main_list)# so here we remove the length of the list fiven by user
    index = None# here we declare the index as None 
    range_for_loop = range(length)# here we give the range  till whn the loop has to run
    for i in range_for_loop:# here we run the for loop till the range of length 
        if query == main_list[i]:# here we chk that weather the query is in the list given by the user
            index = i# if upper condition is true then index becomes i
    return index# this will return i which means index number if the query

u = find_in_list("z", "zoyaa")# here we call the function

def encrypt(plain_msg):# here we make another function to encrypt our msg
    for i in plain_msg:# so here i use for loop in the msg fiven by user
        if i in chars:# so if i means the element of the msg is in chars list
            char_index = find_in_list(i,chars)# then we take a new variable and and call the upper function which we made now with the arguments i means the element of the msg and the list named chars
            new_chr = shifted_chars[char_index]# here we made one more variable  called new+char and declared it as the list of shifted_chars,s index by giving the index as the variable which we made up as char_index so as in both the list we have shifted the character by 2 so as both index will be same but character diff so it will say we will get a new msg
            print ''.join(new_chr), # here new msg will be printed
        else:# if upper condition not true
            print ''.join(i)# same msg will be printed without encrypted
        
encrypt("this will be encrypted because of this function \n")# here we called the function and also wrote \n to start a new line

def decrypt(message):# here  we made a new function to decrypt the encrypted msg
    for i in message:# here we run the loop in the msg
        if i in shifted_chars:# so if element is there in the shifted_chars list
            shifted_chars_index = find_in_list(i,shifted_chars)#here we call the find_in list which will give us the index of the i in the msg
            new_char = chars[shifted_chars_index]# so here we took the variable and gave that element in  chars list index will be the index of the chars_shifted so as in list it is already shiftef so there are different elements in every index of the list
            print ''.join(new_char),# so now the encrypted msg will be decrepted as the characters which were shifted will come back to its own place
        else:# if upper condition is not true 
            print i,# it will print the same msg

decrypt("k nqxg w  \n")# here the encrypted msg is given as an argument and the decrypt function is called

flag = True# so here we declare flag as True
while flag == True:# here we gave the condition that till flag is true this code will keep on running here we will ask the user weather he want to decrypt or encrypt a msg and give him the output
    choice = raw_input("What do u want. encrypt or decrypt in encrypt put 'e' else put 'd' for decrypt :- ")# here we give the option weather he want to encrypt he can press e and for decrypt he can press d
    if choice == 'e':# so if user want to encrypt 
        plain_message = raw_input("Enter message to encrypt?? :-")#he can put the msg now
        encrypt(plain_message)# n now the encrypt function is called with the argument of the msg given by the user so that msg will be encrypted
        print"\n"#here we ask the python to go on a new line
    elif choice == 'd':# so if the user wants to decrypt and he presses d thn
        encrypted_msg = raw_input("Enter message to decrypt? :-")# user is asked to input the msg he wants to decrypt
        decrypt_message(encrypted_msg)# here the decrypt function is called by giving the argument the msg input by the user so the msg will be decrypted
        print "\n"# here we ask pytohn to go to the new line
    play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N) :-")# here we ask the user weather he wants to again encryppt or decrypt msg
    if play_again == 'Y':# if he input Y thn again he will be asked
        continue# this will continue 
    elif play_again == 'N':# if he input N thn code will stop
        break# this will stop the loop
    else:# if upper condition not true loop will come here
        break# and it will call the break function and loop will stop

