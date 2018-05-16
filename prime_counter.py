import math

def is_prime(num):
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime_counter(num):
    numlst = list(range(num+1))
    primelst = list(filter(is_prime,numlst))
    
    if len(primelst) -2 < 0:
        return 0
    else:
        return len(primelst) - 2