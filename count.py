#Code likho jo di gayi list mein jo number 20 se bade hai aur 40 se chote hai unhe count kare. Aur firr unka count print kare.

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0# here we defined the index of the list
count = 0 # this is the variable given to the numbers of the number between the condition given below
while i < len(numbers):# here we give the condition till the loop should continue
    if numbers[i] > 20 and numbers[i] < 40:# here is the condition between wht the numbers wshould be
        count = count +1# this will add the number of numbers fulfilled the condition
    i=i+1# thsi is the increament of the loop
print "the total numbers between 20 and 40 in list of numbers are " + str(count)