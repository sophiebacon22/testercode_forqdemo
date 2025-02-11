class Wallet:

  def __init__(self, initial_amount=0):
    self.balance = initial_amount

  def deposit(self, amount):
    self.balance += amount
    return True
  
  def withdraw(self, amount):
    if not isinstance(amount, (int, float)):
      raise TypeError("Amount must be a number")
    if amount <= 0:
      raise ValueError("Amount must be positive") 
    if self.balance < amount:
      raise ValueError("Insufficient funds")
    self.balance -= amount
    return True