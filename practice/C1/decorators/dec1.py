# 1. Basic Decorator for Logging Function Calls
# Problem: Create a decorator that logs the name of a function
#  and the arguments it was called with. Apply this decorator
#  to a function that adds two numbers.

# Expected Output:
# Calling add(2, 3)
# Result: 5


def log_dec(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}{args}")
        return func(*args, **kwargs)
    return wrapper

@ log_dec
def add(a, b):
    return a+b

print(f"result = {add(2, 3)}")
