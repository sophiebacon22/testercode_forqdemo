class Wallet:

    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientFundsError("Insufficient funds in wallet")
        self.balance -= amount

class InsufficientFundsError(Exception):
    pass