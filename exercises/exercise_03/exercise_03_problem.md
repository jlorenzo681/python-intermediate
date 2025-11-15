# Exercise 3: Lambda Functions and Functional Programming

**Difficulty:** Intermediate

## Objective
Use lambda functions with `map()`, `filter()`, and `sorted()` to process a list of numbers and a list of dictionaries.

## Requirements
1. Create a list of numbers from 1 to 10
2. Use `map()` with a lambda to square each number
3. Use `filter()` with a lambda to get only even numbers
4. Create a list of dictionaries representing products with 'name' and 'price'
5. Use `sorted()` with a lambda to sort products by price

## Expected Output
```
Original numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Squared numbers: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Even numbers: [2, 4, 6, 8, 10]
Products sorted by price:
  Keyboard - $25
  Mouse - $30
  Monitor - $150
```

## Hints
- Lambda syntax: `lambda parameters: expression`
- `map(function, iterable)` applies a function to each element
- `filter(function, iterable)` keeps elements where function returns True
- `sorted(iterable, key=lambda x: x['field'])` sorts by a specific field
- Convert map and filter results to list using `list()`

## Key Concepts
- Lambda (anonymous) functions
- Higher-order functions (map, filter)
- Sorting with custom key functions
- Functional programming concepts
