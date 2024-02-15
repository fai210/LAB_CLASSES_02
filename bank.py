class BankAccount:
    def __init__(self,account_holder,initial_balance=0):
        self.account_holder= account_holder
        self.inital_balance= initial_balance
        
    def depsot (self, account_holder):
        self.inital_balance += account_holder
        return self.inital_balance
    
    def withdraw (self, amount):
        if amount > self.inital_balance:
            raise Exception("insufficient funds")
        self.initial_balance -= amount
        return self.initial_balance
    
    def set_inital_balance(self,amount):
        self.account_holder=amount
    def get_inital_balance (self):
        return self.account_holder
    
    def set_account_holder(self, account_holder):
        self.account_holder = account_holder
    def get_account_holder (self):
        return self.account_holder
    
    
            