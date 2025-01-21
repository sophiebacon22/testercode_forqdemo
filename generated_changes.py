class Wallet:

    def __init__(self, initial_amount):
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient funds") 
        self.balance -= amount