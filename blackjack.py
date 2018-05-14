def blackjack(a,b,c):
    newsum = a+b+c
    if newsum > 21:
        if a == 11 or b == 11 or c == 11:
            newsum-=10
            if newsum > 21:
                print('BUST')
            else:
                return newsum
        else:
            print('BUST')
    else:
        return newsum