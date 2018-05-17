class Account:
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        print(f"{self.owner}'s account created with {self.balance} moneys.")
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
        
    def deposit(self,value):
        self.balance += value
        print(f"A deposit of {value} was made. New balance is {self.balance}")
        ## setuff
        pass
    def withdraw(self,value):
        if (self.balance - value) < 0:
            print(f"Withdraw amount ({value}) higher than available balance ({self.balance})!")
        else:
            self.balance-= value
            print(f"A withdraw of {value} was made. New balance is {self.balance}")
        ##setuff
        pass