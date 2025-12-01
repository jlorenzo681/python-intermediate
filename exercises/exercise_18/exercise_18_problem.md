# Exercise 18: Iterators and the Iterator Protocol SI

**Difficulty:** Advanced

## Objective
Create custom iterators by implementing the iterator protocol (`__iter__` and `__next__`).

## Requirements
1. Create a `Countdown` iterator that counts down from a number
2. Implement `__iter__` and `__next__` methods
3. Raise `StopIteration` when iteration is complete
4. Create a `FibonacciIterator` that generates Fibonacci numbers up to a limit
5. Create an iterator for a custom range with step
6. Demonstrate the difference between iterables and iterators
7. Show that iterators are stateful and can be exhausted

## Expected Output
```
Countdown from 5:
5, 4, 3, 2, 1

Fibonacci up to 100:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

Custom range (0 to 10, step 2):
0, 2, 4, 6, 8, 10

Iterator exhaustion:
First iteration: 1, 2, 3
Second iteration: (empty - iterator exhausted)
```

## Hints
- Implement `__iter__` to return self
- Implement `__next__` to return next value
- Raise StopIteration when done
- Store state in instance variables
- Iterators can only be used once
- iter(obj) calls __iter__, next(it) calls __next__

## Key Concepts
- Iterator protocol
- __iter__ and __next__ methods
- StopIteration exception
- Stateful iteration
- Iterables vs iterators
- Iterator exhaustion
