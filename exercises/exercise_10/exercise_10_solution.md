# Exercise 10: Solution

## Code
```python
import sys


def fibonacci_generator(n):
    """Generate first n Fibonacci numbers."""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def even_numbers(start, end):
    """Generate even numbers in range."""
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num


# 1. Fibonacci generator
print("First 10 Fibonacci numbers:")
fib = fibonacci_generator(10)
print(", ".join(str(x) for x in fib))


# 2. Even numbers generator
print("\nEven numbers from 1 to 20:")
evens = even_numbers(1, 20)
print(", ".join(str(x) for x in evens))


# 3. Manual iteration with next()
print("\nManual iteration:")
fib2 = fibonacci_generator(5)
print(f"Next: {next(fib2)}")
print(f"Next: {next(fib2)}")
print(f"Next: {next(fib2)}")


# 4. Generator expression
print("\nGenerator expression (squares of evens):")
squares_gen = (x**2 for x in range(1, 11) if x % 2 == 0)
print(", ".join(str(x) for x in squares_gen))


# 5. Memory comparison: List vs Generator
def number_list(n):
    """Return a list of numbers (stores all in memory)."""
    return [x for x in range(n)]


def number_generator(n):
    """Yield numbers one at a time (memory efficient)."""
    for x in range(n):
        yield x


# Create large collections
large_list = number_list(10000)
large_gen = number_generator(10000)

list_size = sys.getsizeof(large_list)
gen_size = sys.getsizeof(large_gen)

print(f"\nMemory usage for 10,000 numbers:")
print(f"List: {list_size} bytes")
print(f"Generator: {gen_size} bytes")
print(f"List uses {list_size / gen_size:.1f}x more memory than generator!")
```

## Explanation

**What is a Generator?**
A generator is a function that yields values one at a time instead of returning them all at once. It's like a factory that produces items on demand.

**Yield vs Return:**
```python
# Regular function with return
def get_numbers():
    return [1, 2, 3]  # Creates entire list in memory

# Generator function with yield
def generate_numbers():
    yield 1  # Produces 1
    yield 2  # Then produces 2
    yield 3  # Then produces 3
```

**How Generators Work:**
1. When you call a generator function, it returns a generator object
2. The function code doesn't run yet (lazy!)
3. Each time you call `next()` or iterate, it runs until the next `yield`
4. The state is frozen between yields
5. When the function ends, it raises `StopIteration`

**Lazy Evaluation:**
Generators are lazy - they only produce values when requested. This is memory-efficient for large sequences:

```python
# This stores 1 million numbers in memory
big_list = [x for x in range(1_000_000)]

# This stores just the generator object (~200 bytes)
big_gen = (x for x in range(1_000_000))
```

**Generator State:**
Generators remember their state between yields:
```python
def fibonacci_generator(n):
    a, b = 0, 1  # Initialize once
    while ...:
        yield a  # Pause here, remember a and b
        a, b = b, a + b  # Resume here next time
```

**Generator Expressions:**
Like list comprehensions but with `()` instead of `[]`:
```python
# List comprehension - creates list immediately
squares_list = [x**2 for x in range(10)]

# Generator expression - lazy evaluation
squares_gen = (x**2 for x in range(10))
```

**Infinite Generators:**
Generators can produce infinite sequences:
```python
def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1
```

You can't do this with a list (would run out of memory)!

**When to Use Generators:**
- ✓ Large datasets (don't fit in memory)
- ✓ Expensive computations (calculate on demand)
- ✓ Infinite sequences
- ✓ Pipeline processing (chain generators)
- ✓ Reading large files line by line
- ✗ Need random access (generators are sequential)
- ✗ Need to iterate multiple times (generators exhaust)

**Common Pitfall:**
Generators can only be iterated once:
```python
gen = (x for x in range(3))
list(gen)  # [0, 1, 2]
list(gen)  # [] - generator is exhausted!
```

## Key Concepts

1. **Generators**: Functions that yield values one at a time
2. **yield**: Pause function and return a value, resume later
3. **Lazy Evaluation**: Produce values on demand, not upfront
4. **Memory Efficiency**: Don't store entire sequence
5. **Generator Expressions**: `()` instead of `[]` for lazy lists
6. **State Preservation**: Remember variables between yields
7. **Iterator Protocol**: Generators are iterators
