def capitalizefirsandfifthchars(name):
    i=0
    newname=''
    while i < len(name):
        if i == 0 or i == 4:
            newname+=name[i].upper()
        else:
            newname+=name[i]       
        i+=1
    return newname