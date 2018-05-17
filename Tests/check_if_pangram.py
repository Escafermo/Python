import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    counter = 0
    for i in alphabet:
        if i in str1.lower():
            counter+=1
        else:
            pass
    return counter == 26