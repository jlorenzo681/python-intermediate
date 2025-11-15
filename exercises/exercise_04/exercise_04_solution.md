# Exercise 4: Solution

## Code
```python
def safe_divide(a, b):
    """Safely divide two numbers with error handling."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
        return None
    else:
        print(f"{a} / {b} = {result}")
        print("Division successful!")
        return result
    finally:
        print("Operation complete.\n")

# Test cases
print("Test 1:")
safe_divide(10, 2)

print("Test 2:")
safe_divide(10, 0)

print("Test 3:")
safe_divide(10, 'abc')
```

## Explanation

**Try Block:**
The `try:` block contains code that might raise an exception. Here, division might fail in several ways.

**Except Blocks:**
Each `except` catches a specific exception type:
- `ZeroDivisionError`: Raised when dividing by zero
- `TypeError`: Raised when trying to divide incompatible types (number by string)

**Else Block:**
The `else:` block runs ONLY if no exception was raised in the try block. This is where we put success messages and return the result.

**Finally Block:**
The `finally:` block ALWAYS runs, whether an exception occurred or not. It's perfect for cleanup code like closing files or printing completion messages.

**Control Flow:**
1. Try the division
2. If exception occurs → jump to matching except block → skip else → run finally
3. If no exception → run else → run finally

**Why Not Just Use Try-Except?**
- `else` makes it clear what code depends on success
- `finally` ensures cleanup happens even if you return early
- Code is more readable and maintainable

**Multiple Exceptions:**
You can catch multiple exceptions in one line:
```python
except (ZeroDivisionError, TypeError) as e:
    print(f"Error: {e}")
```

Or handle them separately for different messages (as we did).

## Key Concepts

1. **Try-Except**: Catch and handle exceptions gracefully
2. **Specific Exceptions**: Catch specific types rather than bare `except:`
3. **Else Clause**: Code that runs only when no exception occurs
4. **Finally Clause**: Code that always runs (cleanup)
5. **Defensive Programming**: Anticipate and handle potential errors
6. **Exception Types**: Different exceptions for different error conditions
