# 2. Timing a Function Execution
# Problem: Write a decorator that measures the time taken
# by a function to execute. Use this decorator to time a 
# function that calculates the factorial of a number.

# Expected Output:
# Executing factorial took 0.0001 seconds

import time
import functools

def time_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"Executing {func.__name__} took {t2 - t1:.4f} seconds")
        return result
    return wrapper

@time_func
def factorial(n):
    def fact(n):
        return 1 if n==0 else n * fact(n-1)

factorial(5)


