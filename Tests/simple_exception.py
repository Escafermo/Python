def sqrt_expect_num ():
    while True:
        try:
            userinput = int(input('Input a number: '))
            print(f'The sqrt of {userinput} is '+str(userinput**2))
        except:
            print("Wrong variable type, expecting a number!")
            continue
        else:
            print("Thank you")
            break
sqrt_expect_num()