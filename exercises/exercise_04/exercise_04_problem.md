# Exercise 4: Exception Handling

**Difficulty:** Intermediate

## Objective
Create a program that safely handles user input for division operations, catching and handling potential errors.

## Requirements
1. Create a function `safe_divide(a, b)` that divides two numbers
2. Handle `ZeroDivisionError` when dividing by zero
3. Handle `ValueError` when converting non-numeric strings
4. Handle `TypeError` when wrong types are passed
5. Use a `try-except-else-finally` block
6. Test the function with valid input, zero division, and invalid input

## Expected Output
```
Test 1: 10 / 2 = 5.0
Division successful!
Operation complete.

Test 2: 10 / 0
Error: Cannot divide by zero!
Operation complete.

Test 3: 10 / 'abc'
Error: Invalid input type. Please provide numbers.
Operation complete.
```

## Hints
- Use `try:` to wrap code that might raise exceptions
- Use `except ExceptionType:` to catch specific exceptions
- Use `else:` for code that runs if no exception occurred
- Use `finally:` for code that always runs (cleanup)
- Multiple except blocks can catch different exception types

## Key Concepts
- Try-except blocks
- Multiple exception types
- Else and finally clauses
- Error messages and handling
- Defensive programming
