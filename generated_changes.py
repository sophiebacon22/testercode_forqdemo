# Represents a wallet that holds cash
class Wallet:
    
    def __init__(self):
        """Initialize the wallet with 0 cash"""
        self.cash = 0
        
    def add_cash(self, amount):
        """Add cash to the wallet
        
        Args:
            amount (int): The amount of cash to add
        """
        self.cash += amount
        
    def spend_cash(self, amount):
        """Spend an amount of cash from the wallet
        
        Args:
            amount (int): The amount of cash to spend
        """
        if self.cash < amount:
            print("Not enough cash in wallet")
            return
        self.cash -= amount