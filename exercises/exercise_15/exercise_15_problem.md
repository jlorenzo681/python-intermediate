# Exercise 15: Magic Methods (Dunder Methods)

**Difficulty:** Advanced

## Objective
Implement magic methods to make custom classes behave like built-in types.

## Requirements
1. Create a `Vector2D` class representing a 2D vector
2. Implement `__init__`, `__str__`, and `__repr__`
3. Implement arithmetic operators: `__add__`, `__sub__`, `__mul__` (scalar multiplication)
4. Implement comparison operators: `__eq__`, `__lt__`, `__le__`
5. Implement `__len__` (magnitude) and `__abs__` (absolute value)
6. Implement `__getitem__` and `__setitem__` for indexing (v[0], v[1])
7. Demonstrate all magic methods with examples

## Expected Output
```
Vector v1: Vector2D(3, 4)
String representation: Vector(3, 4)

Vector arithmetic:
v1 + v2 = Vector(5, 7)
v1 - v2 = Vector(1, 1)
v1 * 2 = Vector(6, 8)

Comparison:
v1 == Vector(3, 4): True
v1 < v2: False

Length and absolute value:
Magnitude of v1: 5.0
abs(v1): 5.0

Indexing:
v1[0] = 3
v1[1] = 4
After setting v1[0] = 10: Vector(10, 4)

Iteration:
Components: 10, 4
```

## Hints
- `__str__`: user-friendly string (print)
- `__repr__`: developer-friendly string (debugging)
- `__add__`: addition with +
- `__eq__`: equality with ==
- `__lt__`: less than with <
- `__len__`: length with len()
- `__getitem__`: indexing with []
- Return new objects for arithmetic (don't modify self)

## Key Concepts
- Magic methods (dunder methods)
- Operator overloading
- Making classes behave like built-in types
- Special method protocols
- Comparison and arithmetic
- Indexing and iteration
