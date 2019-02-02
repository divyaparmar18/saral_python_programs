ascii_value = ord("v") # 118
string_value = chr(ascii_value) # v

def encrypt():
    message = raw_input("enter the msg u want to encrypt : ")
    ascii_msg = [ord(char) + 3  for char in message]
    encrypt_msg = [chr(char) for char in ascii_msg ]
    print ''.join (encrypt_msg)

encrypt()

def decrypt():
  message = raw_input("Enter the message you want to decrypt")
  ascii_message = [ord(char) - 3 for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print ''.join(decrypt_message)


decrypt()

flag = True
while flag == True:
    choice = raw_input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
    if choice == 'E':
      encrypt()
    elif choice == 'D':
      decrypt()    
    else:
      play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)")
      if play_again == 'Y':
        continue
      elif play_again == 'N':
        break