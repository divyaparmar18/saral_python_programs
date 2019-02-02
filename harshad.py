def list_change(list_1,list_2):
    i=0
    while i < len(list_1):
        result = list_1[i]*list_2[i]
        print result
        i=i+1
    


final = list_change([2,3,10,5,8],[10,4,35,2,4])
print final
