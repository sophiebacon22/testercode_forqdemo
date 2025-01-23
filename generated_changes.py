# Add a helper function to validate amount is positive
def validate_positive(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
        
# Update deposit to validate amount first
def deposit(amount):
    validate_positive(amount)  
    balance = get_balance()
    balance += amount
    set_balance(balance)

# Update withdraw to validate amount first  
def withdraw(amount):
    validate_positive(amount)
    balance = get_balance()
    if amount > balance:
        raise ValueError("Insufficient funds")
    balance -= amount
    set_balance(balance)

# Update transfer to validate both amounts first
def transfer(amount, recipient):
    validate_positive(amount)
    validate_positive(recipient.get_balance())
    balance = get_balance()
    if amount > balance:
        raise ValueError("Insufficient funds")
    balance -= amount
    recipient.deposit(amount)
    set_balance(balance)