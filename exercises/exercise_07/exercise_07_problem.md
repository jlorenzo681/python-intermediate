# Exercise 7: Function Decorators

**Difficulty:** Intermediate+

## Objective
Create and use decorators to add functionality to functions without modifying their code.

## Requirements
1. Create a `timer` decorator that measures function execution time
2. Create a `logger` decorator that logs when a function is called
3. Apply decorators to a simple function that calculates factorial
4. Demonstrate using multiple decorators on the same function (stacking)
5. Show the output with timing and logging information

## Expected Output
```
Calling function: factorial
factorial(5) took 0.0001 seconds
Result: 120

Calling function: slow_function
slow_function() took 1.0023 seconds
Result: Done!
```

## Hints
- Decorator syntax: `@decorator_name` above function definition
- Decorator structure: a function that takes a function and returns a function
- Use `time.time()` to measure execution time
- Use `functools.wraps` to preserve function metadata
- Stack decorators by using multiple @ lines

## Key Concepts
- Decorators as higher-order functions
- Function wrapping
- Closures
- The @ syntax
- Decorator stacking
