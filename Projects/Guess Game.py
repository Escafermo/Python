guesslst = [0]
from random import randint
myrandomnum = randint(1,100)

while True:
    guess = int(input('What is your guess: ' ))
    if guess > 100 or guess < 1:
        print("Invalid!")
        continue
    if guess == myrandomnum:
        print("Crongatulations!")
        print("My random number was: " + str(myrandomnum))
        print("You took " + str(len(guesslst)) + " attempts.")
        break
    
    guesslst.append(guess)

    
    if guesslst[-2]:
        if abs(myrandomnum-guess) < abs(myrandomnum-guesslst[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
        
    else:
        if abs(myrandomnum-guess) <= 10:
            print("Warm!")
        else:
            print("Cold!")