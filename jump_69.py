def jump_69(arr):
    i=0
    newsum = 0
    while i < len(arr):
        if arr[i]==6:
            while arr[i]!=9:
                i+=1
        else:
            newsum+=arr[i]
        i+=1
    return newsum