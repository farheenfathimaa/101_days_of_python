# Decorator to Retry a Function on Failure

# Problem: Create a decorator that retries a function a 
# specified number of times if it raises an exception. 
# Use this decorator on a function that may randomly fail,
# such as simulating a network request.
# Requirements:
# The decorator should accept an argument specifying the 
# maximum number of retries.
# It should retry the function if an exception occurs.

# Example Usage:
# @retry_decorator(max_retries=3)
# def unstable_function():
#     # Simulates random failures

import random

def retry_decorator(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {retries + 1} failed: {e}")
                    retries += 1
            print(f"All {max_retries} retries failed.")
        return wrapper
    return decorator
       
@retry_decorator(max_retries=3)
def unstable_function():
    # Simulates random failures
    if random.random() < 0.5:
        raise ValueError("Random failure occured.")
    else:
        print("Function succeeded.")

unstable_function()

