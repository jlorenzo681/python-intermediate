# Exercise 4: Exception Handling
# Objective: Create a safe division function with proper error handling

# Hints:
# - Use try: for code that might raise exceptions
# - Use except ExceptionType: to catch specific exceptions
# - Use else: for code that runs if no exception occurred
# - Use finally: for code that always runs
# - Common exceptions: ZeroDivisionError, TypeError, ValueError

# Your code here:

def safe_divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print(f'{a} / {b}\nError: Cannot divide by zero!')
    except ValueError:
        print(f'{a} / {b}\nError: Invalid value.')
    except TypeError:
        print(f'{a} / {b}\nError: Invalid input type. Please provide numbers.')
    else:
        print(f'{a} / {b} = {result}\nDivision successful!')
    finally:
        print("Operation complete.")

print(f'Test 1: ')
safe_divide(10,2)

print(f'Test 2: ')
safe_divide(10,0)

print(f'Test 3: ')
safe_divide(10,"abc")
