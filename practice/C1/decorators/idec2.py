# Decorator to Enforce Rate-Limiting on Function Calls

# Problem: Implement a decorator that limits the number 
# of times a function can be called within a specified 
# time period. For example, only allow the function to 
# be called 3 times every 5 seconds.
# Requirements:
# The decorator should accept arguments specifying the 
# maximum calls and the time window (in seconds).
# If the limit is exceeded, the function should raise 
# an exception or print a message indicating that the 
# rate limit has been reached.

# Example Usage:
# @rate_limiter(max_calls=3, time_window=5)
# def fetch_data():
#     # Function that fetches data from a source

import time
from collections import deque
def rate_limiter(max_calls, time_window):
    def decorator(func):
        call_times = deque() # to store timestamps of recent calls
        def wrapper(*args, **kwargs):
            current_time = time.time()

            # Remove outdated calls
            while call_times and current_time - call_times[0] > time_window:
                call_times.popleft()
            
            if len(call_times) < max_calls:
                call_times.append(current_time)
                return func(*args, **kwargs)
            else:
                print("Rate limit exceeded. Please try again later.")
        return wrapper
    return decorator

@rate_limiter(max_calls=3, time_window=5)
def fetch_data():
    print("Fetching data...")

for _ in range(5):
    fetch_data()
    time.sleep(1)