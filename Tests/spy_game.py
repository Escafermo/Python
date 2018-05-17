def spy_game(nums):
    lookingfor = ([0,0,7,'x'])
    
    for eachnum in nums:
        if eachnum == lookingfor[0]:
            lookingfor.pop(0)
    
    return len(lookingfor) == 1