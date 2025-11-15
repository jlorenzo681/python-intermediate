# Exercise 18: Solution

## Code
```python
class Countdown:
    """Iterator that counts down from a number."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        """Return the iterator object (self)."""
        return self

    def __next__(self):
        """Return the next value."""
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


class FibonacciIterator:
    """Iterator for Fibonacci numbers up to a limit."""

    def __init__(self, max_value):
        self.max_value = max_value
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max_value:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value


class CustomRange:
    """Custom range with start, stop, and step."""

    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


# Test Countdown
print("Countdown from 5:")
countdown = Countdown(5)
print(", ".join(str(x) for x in countdown))

# Test Fibonacci
print("\nFibonacci up to 100:")
fib = FibonacciIterator(100)
print(", ".join(str(x) for x in fib))

# Test CustomRange
print("\nCustom range (0 to 10, step 2):")
custom = CustomRange(0, 10, 2)
print(", ".join(str(x) for x in custom))

# Demonstrate exhaustion
print("\nIterator exhaustion:")
numbers = Countdown(3)
print(f"First iteration: {', '.join(str(x) for x in numbers)}")
print(f"Second iteration: {', '.join(str(x) for x in numbers)} (empty - exhausted)")
```

## Key Concepts
- __iter__: Returns iterator object
- __next__: Returns next value or raises StopIteration
- Stateful: Remembers position
- Single-use: Can't reset without creating new iterator
- Protocol: Interface for iteration
