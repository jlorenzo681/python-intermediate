# Exercise 7: Function Decorators
# Objective: Create decorators to add functionality to functions

# Hints:
# - Decorator structure: def decorator(func): def wrapper(*args, **kwargs): ...
# - Use @decorator_name above function definition
# - Import wraps: from functools import wraps
# - Use @wraps(func) on wrapper to preserve metadata
# - Stack decorators with multiple @ lines

# Your code here:

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time.sleep(1)
        time_end = time.time()
        elapse = time_end - time_start
        print(f"{func.__name__}({','.join(map(str,args))}) took {elapse:.4f} seconds")
        return result
    return wrapper

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwards):
        print(f'Calling funtion: {func.__name__}')
        result = func(*args, **kwards)
        return result
    return wrapper

@timer
@logger    
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

@timer
@logger
def slow_function():
    time.sleep(1)
    return "Done!"


result1 = factorial(5)
print(f'Result: {result1}')

result2 = slow_function()
print(f'Result: {result2}')