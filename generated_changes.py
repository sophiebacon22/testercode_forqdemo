# Add a helper function to validate amount is positive
def validate_positive(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
        
# Wrap existing money operations in try/except blocks
# and call validate_positive on amounts

try:
    validate_positive(amount)
    # Existing deposit logic
except ValueError as e:
    print(e)
    
try: 
    validate_positive(amount)
    # Existing withdraw logic 
except ValueError as e:
    print(e)

try:
    validate_positive(amount)
    # Existing transfer logic
except ValueError as e:
    print(e)