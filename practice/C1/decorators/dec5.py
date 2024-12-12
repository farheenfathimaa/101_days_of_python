# 5. Cashing Function Results
# Problem: Implement a decorator that caches the results 
# of a function call to avoid recomputation if the same 
# arguments are passed again. Test it with a function that
# squares a number.

# Expected Output:
# Computing square(4)
# Result: 16
# Using cached result for square(4)
# Result: 16

def cache(func):
    cache={}
    def wrapper(n):
        if n not in cache:
            print(f"Computing {func.__name__}({n})")
            cache[n] = func(n)
        else:
            print(f"Using cached result for {func.__name__}({n})")
        return cache[n]
    return wrapper

@cache
def square(n):
    return n*n

print(f"Result: {square(4)}")
print(f"Result: {square(4)}")