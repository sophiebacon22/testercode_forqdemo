class Wallet:
    
    def __init__(self):
        self.balance = 0
        self.transaction_history = []
        
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append({"type": "deposit", "amount": amount})
        
    def withdraw(self, amount):
        self.balance -= amount
        self.transaction_history.append({"type": "withdrawal", "amount": amount})
        
    def get_transaction_history(self):
        return self.transaction_history