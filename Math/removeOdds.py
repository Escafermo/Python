def isEven (*args):
    i=0
    lst = []
    
    while i < len(args): 
        if (args[i])%2==0:
            lst.append(args[i])
        i+=1
    return lst

mynumber = int(input('Check if this number is even : ' ))
print(isEven(mynumber))

# NOT WORKING PROPERLY, WANT TO PASS IN TUPLES VIA INPUT AND NOT INT