def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: division by zero")
        result = None
    return result