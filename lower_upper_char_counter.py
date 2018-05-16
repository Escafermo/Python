def up_low(s):
    uppercounter=0
    lowercounter=0
    for char in s:
        if char.isupper():
            uppercounter+=1
        elif char.islower():
            lowercounter+=1
    print('No. of Upper case characters: '+ str(uppercounter))
    print('No. of Lower case characters: '+ str(lowercounter))