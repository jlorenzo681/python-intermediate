# Exercise 10: Generators and Yield

**Difficulty:** Intermediate+

## Objective
Create generators using `yield` to efficiently produce sequences without storing entire collections in memory.

## Requirements
1. Create a generator function that yields Fibonacci numbers
2. Create a generator that yields even numbers from a range
3. Demonstrate lazy evaluation by showing memory efficiency
4. Use `next()` to manually iterate through a generator
5. Create a generator expression (like list comprehension but lazy)
6. Show the difference between returning a list vs yielding values

## Expected Output
```
First 10 Fibonacci numbers:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Even numbers from 1 to 20:
2, 4, 6, 8, 10, 12, 14, 16, 18, 20

Manual iteration:
Next: 0
Next: 1
Next: 1

Generator expression (squares of evens):
4, 16, 36, 64, 100

List uses more memory than generator!
```

## Hints
- Use `yield` instead of `return` in generator functions
- Generators are lazy - values produced on demand
- Use `next(generator)` to get next value
- Generator expression: `(x for x in range(10))`
- Generators can only be iterated once
- Use `sys.getsizeof()` to compare memory usage

## Key Concepts
- Generator functions and yield
- Lazy evaluation
- Memory efficiency
- Iterator protocol
- Generator expressions
- Infinite sequences
