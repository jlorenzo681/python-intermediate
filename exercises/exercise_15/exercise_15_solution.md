# Exercise 15: Solution

## Code
```python
import math


class Vector2D:
    """2D vector with magic methods."""

    def __init__(self, x, y):
        """Initialize vector with x and y components."""
        self.x = x
        self.y = y

    def __str__(self):
        """User-friendly string representation."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Developer-friendly string representation."""
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        """Add two vectors."""
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract two vectors."""
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Multiply vector by scalar."""
        return Vector2D(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        """Check if two vectors are equal."""
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """Compare vector magnitudes (less than)."""
        return self.magnitude() < other.magnitude()

    def __le__(self, other):
        """Compare vector magnitudes (less than or equal)."""
        return self.magnitude() <= other.magnitude()

    def __abs__(self):
        """Return magnitude of vector."""
        return self.magnitude()

    def __len__(self):
        """Return magnitude as integer."""
        return int(self.magnitude())

    def __getitem__(self, index):
        """Get component by index (0=x, 1=y)."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range (0-1)")

    def __setitem__(self, index, value):
        """Set component by index."""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range (0-1)")

    def __iter__(self):
        """Make vector iterable."""
        return iter([self.x, self.y])

    def magnitude(self):
        """Calculate vector magnitude."""
        return math.sqrt(self.x**2 + self.y**2)


# Demonstration
v1 = Vector2D(3, 4)
v2 = Vector2D(2, 3)

# __repr__ and __str__
print(f"Vector v1: {repr(v1)}")
print(f"String representation: {str(v1)}")

# Arithmetic operations
print("\nVector arithmetic:")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")

# Comparison
print("\nComparison:")
print(f"v1 == Vector(3, 4): {v1 == Vector2D(3, 4)}")
print(f"v1 < v2: {v1 < v2}")

# Length and absolute value
print("\nLength and absolute value:")
print(f"Magnitude of v1: {v1.magnitude()}")
print(f"abs(v1): {abs(v1)}")

# Indexing
print("\nIndexing:")
print(f"v1[0] = {v1[0]}")
print(f"v1[1] = {v1[1]}")
v1[0] = 10
print(f"After setting v1[0] = 10: {v1}")

# Iteration
print("\nIteration:")
print(f"Components: {', '.join(str(x) for x in v1)}")
```

## Explanation

**Magic Methods (Dunder Methods):**

"Dunder" = "double underscore". These special methods let you define how your class interacts with Python operators and built-in functions.

**Common Categories:**

**1. String Representation:**
- `__str__`: Called by `str()` and `print()` - user-friendly
- `__repr__`: Called by `repr()` - should be valid Python code

```python
v = Vector2D(3, 4)
print(v)        # Uses __str__: "Vector(3, 4)"
repr(v)         # Uses __repr__: "Vector2D(3, 4)"
```

**2. Arithmetic Operators:**
- `__add__(self, other)`: `a + b`
- `__sub__(self, other)`: `a - b`
- `__mul__(self, other)`: `a * b`
- `__truediv__(self, other)`: `a / b`
- `__mod__(self, other)`: `a % b`
- `__pow__(self, other)`: `a ** b`

Return a new object, don't modify self!

**3. Comparison Operators:**
- `__eq__(self, other)`: `a == b`
- `__ne__(self, other)`: `a != b`
- `__lt__(self, other)`: `a < b`
- `__le__(self, other)`: `a <= b`
- `__gt__(self, other)`: `a > b`
- `__ge__(self, other)`: `a >= b`

**4. Container Emulation:**
- `__len__(self)`: `len(obj)`
- `__getitem__(self, key)`: `obj[key]`
- `__setitem__(self, key, value)`: `obj[key] = value`
- `__delitem__(self, key)`: `del obj[key]`
- `__contains__(self, item)`: `item in obj`
- `__iter__(self)`: `for x in obj`

**5. Other Important Ones:**
- `__init__(self, ...)`: Constructor
- `__del__(self)`: Destructor
- `__call__(self, ...)`: Make object callable like function
- `__bool__(self)`: Truthiness testing
- `__hash__(self)`: Make object hashable (for dict keys)

**Operator Overloading:**

```python
v1 + v2  # Python calls v1.__add__(v2)
v1 == v2  # Python calls v1.__eq__(v2)
v1[0]    # Python calls v1.__getitem__(0)
```

**Making Objects Iterable:**

```python
def __iter__(self):
    return iter([self.x, self.y])
```

Now you can:
```python
for component in v1:
    print(component)
```

**Important Design Principles:**

1. **Immutability for Math Operations:**
   ```python
   def __add__(self, other):
       return Vector2D(...)  # New object
       # NOT: self.x += other.x; return self
   ```

2. **Consistency with Built-ins:**
   If your class represents a number, make `+`, `-`, `*` work.
   If it's a container, make indexing and `len()` work.

3. **Return NotImplemented:**
   ```python
   def __add__(self, other):
       if not isinstance(other, Vector2D):
           return NotImplemented  # Let Python try other.__radd__
       return Vector2D(...)
   ```

**Common Magic Methods:**

```python
__init__     # Constructor
__str__      # String representation
__repr__     # Developer representation
__eq__       # Equality
__lt__       # Less than
__len__      # Length
__getitem__  # Indexing
__iter__     # Iteration
__call__     # Make callable
__enter__    # Context manager entry
__exit__     # Context manager exit
```

**When to Use:**

- ✓ Making custom classes feel like built-in types
- ✓ Natural, intuitive interfaces
- ✓ Mathematical objects (vectors, matrices, complex numbers)
- ✓ Container classes
- ✗ Don't override without good reason
- ✗ Don't make operators do unexpected things

## Key Concepts

1. **Magic Methods**: Special methods with double underscores
2. **Operator Overloading**: Define behavior for operators
3. **Protocol**: Set of magic methods for specific behavior
4. **__str__ vs __repr__**: User vs developer representation
5. **Container Protocol**: `__len__`, `__getitem__`, `__iter__`
6. **Comparison Protocol**: `__eq__`, `__lt__`, etc.
7. **Immutability**: Return new objects for operations
