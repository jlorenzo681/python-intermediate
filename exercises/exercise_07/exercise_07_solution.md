# Exercise 7: Solution

## Code
```python
import time
from functools import wraps


def timer(func):
    """Decorator that measures execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"{func.__name__}({', '.join(map(str, args))}) took {elapsed:.4f} seconds")
        return result
    return wrapper


def logger(func):
    """Decorator that logs function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper


# Apply decorators using @ syntax
@logger
@timer
def factorial(n):
    """Calculate factorial of n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


@logger
@timer
def slow_function():
    """A function that takes some time."""
    time.sleep(1)
    return "Done!"


# Test the decorated functions
result1 = factorial(5)
print(f"Result: {result1}\n")

result2 = slow_function()
print(f"Result: {result2}")
```

## Explanation

**What is a Decorator?**
A decorator is a function that takes another function and extends its behavior without modifying it directly. It's a way to "wrap" functionality around existing functions.

**Decorator Structure:**
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper
```

**How It Works:**
1. `@timer` above a function is equivalent to: `factorial = timer(factorial)`
2. The decorator returns a new function (wrapper) that replaces the original
3. When you call `factorial(5)`, you're actually calling `wrapper(5)`
4. The wrapper calls the original function and adds extra behavior

**The @wraps Decorator:**
`@wraps(func)` from functools preserves the original function's metadata (name, docstring, etc.). Without it, `factorial.__name__` would be "wrapper" instead of "factorial".

**Stacking Decorators:**
```python
@logger
@timer
def factorial(n):
    ...
```

This is equivalent to: `factorial = logger(timer(factorial))`

Order matters! The decorators are applied from bottom to top:
1. `timer` wraps `factorial` first (adds timing)
2. `logger` wraps the result (adds logging)

When called: logger wrapper → timer wrapper → original function

**Why Use Decorators?**
- **DRY Principle**: Add common functionality (logging, timing, auth) without duplicating code
- **Separation of Concerns**: Keep business logic separate from cross-cutting concerns
- **Reusability**: Apply the same decorator to many functions
- **Clean Code**: `@timer` is more readable than manually wrapping functions

**Common Use Cases:**
- Logging and debugging
- Timing/profiling
- Authentication/authorization
- Caching/memoization
- Input validation
- Rate limiting

## Key Concepts

1. **Decorators**: Functions that modify other functions
2. **Higher-Order Functions**: Functions that take/return functions
3. **Closures**: Inner functions that remember outer function variables
4. **@syntax**: Syntactic sugar for applying decorators
5. **functools.wraps**: Preserve function metadata
6. **Decorator Stacking**: Applying multiple decorators to one function
