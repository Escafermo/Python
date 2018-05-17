def lower_upper_string (mystring):
    i=0
    newstring = ''
    
    while i < len(mystring):
        
        if (i)%2==0:
            newstring+=mystring[i].upper()
        else:
            newstring+=mystring[i].lower()      
        i+=1
    return newstring

mystring = input('Interpolate lowercase and uppercase: ' )
print(lower_upper_string(mystring))