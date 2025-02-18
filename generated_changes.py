class Wallet:
    
    def __init__(self):
        self.balances = {}
        
    def add_balance(self, currency, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.balances[currency] = amount
        
    def get_balance(self, currency):
        return self.balances.get(currency, 0) 

# Additional methods 
        
# Modify add_balance to check for positive amount
def add_balance(self, currency, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    self.balances[currency] = amount

# Add validation to any other methods that update balances
def withdraw(self, currency, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if self.get_balance(currency) < amount:
        raise ValueError("Insufficient funds")
    self.balances[currency] -= amount