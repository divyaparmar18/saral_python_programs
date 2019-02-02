
def find_in_list(query,main_list):
    length = len(main_list)
    range_for_loop = range(length)
    index = None 
    for i in range_for_loop:
        if query == main_list[i]:
            index = i
    return index

c = find_in_list("zoyaa",["zoyaa","divya","pratik","danny"])
#print c

chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

# encrypt_message function defined here but not called
def encrypt_message(plain_msg):
# this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
    for character in plain_msg:
      # for character in msg
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            print new_char,
        else:
           print character,
    
encrypt_message("shinuu ek pagal ladka hai \n")

def decrypt_message(encrypted_msg):
# this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
    for character in encrypted_msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            print new_char,
        else:
            print character,

decrypt_message("ogtc pcco fkxac jck \n")


flag = True
while flag == True:
    choice = raw_input("What do u want. encrypt or decrypt in encrypt put 'e' else put 'd' for decrypt :- ")
    if choice == 'e':
        plain_message = raw_input("Enter message to encrypt?? :-")
        encrypt_message(plain_message)
        print"\n"
    elif choice == 'd':
        encrypted_msg = raw_input("Enter message to decrypt? :-")
        decrypt_message(encrypted_msg)
        print "\n"
    play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N) :-")
    if play_again == 'Y':
        continue
    elif play_again == 'N':
        break
    else:
        break
