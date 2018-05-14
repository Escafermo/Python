def has_33(nums):
    i=0
    while i +1 < len(nums):
        if nums[i+1] == 3 and nums[i] == 3:
            return True
        else:
            return False
        i+=1