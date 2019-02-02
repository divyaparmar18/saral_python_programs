#print "We will learn debugging by removing all the errors from this python file.
print "We will learn debugging by removing all the errors from this python file."

"""year = 2016
name = "NavGurukul"
print name + ', ' +   + "mein start hua tha!"""
#debug this program#


year = 2016
name = "NavGurukul"
print name + ', ' + str(year )  + " mein start hua tha!"# this had a bug to add integer and string which pytohn dosent understand and shows error so here i converted the int into string

"""price_milk = raw_input("1L milk ka price daalo?")
print "10L milk " + price_milk*10 + " rupees ka aata hai."""# here it is taking input as a string so as the total price is multiplying with ten then it shows 10for ten times bcoz its a string so we need to convert the raw_input into integer

price_milk = raw_input("1L milk ka price daalo?")
price = int(price_milk)#so here i converted the price into integer
total = price * 10#then here i multiplied the price to 10 and stored into a variableso here we print total price 
print "10L milk " + str(total) + " rupees ka aata hai."# so we print the total

"""number = raw_input("please enter a decimal number")
print "your number divided by 2 is equal to = " + number/2"""

number = raw_input("please enter a decimal number:")# here we take a raw_input as a string from user
num = float(number)# we converted it into a float as it was showing error bcoz string cannot be divided by float
print "your number divided by 2 is equal to = " + str(num/2)Z# so here we wrote the result

"""#Tumhare paas 5 mangoes hai
mangoes = 5
# Kisi ne humhe 5 aur mangoes de diye
manGoes = mangoes + 5
# Ab tumne unn mangoes ko 5 logo mei baant diya
print mangoes / 5#this line is not correct as pytohn is case sensetive mangoes and manGoes is different for it 
# Par isse toh 1 mango hi mila. Par milne 2 chahiye the. Code ko sahi karo jisse ki sabko sahi mangoes mile."""
mangoes = 5
manGoes = mangoes+5
print manGoes/5

"""# Aapke paas ek variable mein `raw_input` se gaadi ki speed ka ek integer hai
speed = int( raw_input("Gaadi ki speed daalo > ") )

# Ab aapne speed check kar ke kuch print karna hai:
# Agar 60 se kam hai toh print karna: "Speed kam hai"
# Agar 30 se kam hai toh print karna: "Speed bahot kam hai"
# Agar 100 se zyada hai toh print karo: "Bahot zyada hai"
if speed < 60:
    print "Speed kam hai"
elif speed < 30:
    print "Speed bahot kam hai"
elif speed > 100:
    print "Speed bahot fast hai"

# Isme ek baar speed 20 daal ke dekho aur dekho ki "Speed bahot kam" hai ki
# output aati hai ya nahi. Agar nahi aati toh isko theek karo aur yeh socho
# ki kya problemn hai."""
speed = int( raw_input("Gaadi ki speed daalo > ") )# here we take the input from the user as the speed of thew bike
if speed <= 30:# here we give the condition that 
    print ("speed bahot kam hai")# if the condition is true it will pritn it
elif speed > 30 and speed <=60:# here it will chk weather the speed ois bewtween 30 and 60
    print ("speed kam hai")# if givewn condition is true then this will print
elif speed > 60 and speed <= 100:# this will chk the condition weather its true or false
    print ("speed achi hai")# if the given condition is true it will print this
elif speed > 100:#condition is given 
    print ("speed bahot hai")#if condition is true then it will print this

"""# `raw_input` ka use kar ke user se din aur abhi ka samay (lunch, dinner) input
# leke uss samay ka menu print karvana hai. Abhi hum sirf monday aur tuesday ke
# liye likh rahe hain
# Monday aur Tuesday dono time daal roti banegi, bas Tuesday raat ko Pav Bhaji banegi
# Neeche waale program mein jab tuesday daalte ho toh pav bhaji print nahi hota.
# Isko sahi karo.
day = raw_input("Aaj ka din kya hai? (monday/tuesday) > ")
time = raw_input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
if day == "monday" or day == "tuesday":
    print "Daal-Roti banegi aaj"
elif day == "tuesday" and time == "dinner":
    print "Pav-Bhaji banegi aaj toh :)"w"""#in this code there is a error bcoz it first condition becomes true and it prints dal roti and it dosent go to the next condition

# `raw_input` ka use kar ke user se din aur abhi ka samay (lunch, dinner) input
# leke uss samay ka menu print karvana hai. Abhi hum sirf monday aur tuesday ke
# liye likh rahe hain
# Monday aur Tuesday dono time daal roti banegi, bas Tuesday raat ko Pav Bhaji banegi
# Neeche waale program mein jab tuesday daalte ho toh pav bhaji print nahi hota.
# Isko sahi karo.
day = raw_input("Aaj ka din kya hai? (monday/tuesday) > ")#user inputs the day
time = raw_input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")#user inputs the time
if day == "monday" or day == "tuesday" and time == "lunch":#here we give the condition that if it is monday or tuesday and lunch then print dal roti
    print "Daal-Roti banegi aaj"# this will get print if upper condition is true
elif day == "tuesday" and time == "dinner":#here we give the condition that if day is tuesday and time is dinner we will cook pav bhaji
    print "Pav-Bhaji banegi aaj toh :)"# this will print if upper condition is true