password = raw_input("enter a password : ")# here we take the password from the user
if len(password) > 5 and len(password) <= 16:# here we give the condition that wht its length should be
    if "$" in password and  "2" in password or "8" in password and "A" in password or "Z" in password:# here we give all the condition that has to be in password
        print "Strong password"# if every condition is done thn it will print this
    else:# if all the condition are not true
        print "Weak password"#this will print
else:# if the length is not as per the condition we comes here
    print "the password should be between 6 and 16 letters"#this gets printed

