class Account:
    def __init__(self, balance=0):
        self.balance = balance
        
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Error: Insufficient funds")
            
    def deposit(self, amount):
        self.balance += amount

account = Account(100)
account.withdraw(120) # Prints error
account.deposit(50)
account.withdraw(80) # Withdraws successfully