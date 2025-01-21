def divide(a, b):
    # Add input validation
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an int or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an int or float")
    if b == 0:
        raise ValueError("b cannot be zero")
    
    return a / b