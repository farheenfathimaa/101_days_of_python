# 4. Counting Function Calls
# Problem: Create a decorator that counts how many times 
# a function has been called. Use it on a function that 
# returns a greeting message.

# Expected Output:
# greet() has been called 1 times
# greet() has been called 2 times

def count(func):
    def wrapper():
        wrapper.calls +=1
        print(f"{func.__name__}() has been called {wrapper.calls} times")
        return func()
    wrapper.calls = 0
    return wrapper

@count
def greet():
    print("Hello!")

greet()
greet()
greet()
greet()