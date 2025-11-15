# Exercise 5: Solution

## Code
```python
from collections import namedtuple
import math

# Working with regular tuples
point = (3, 4)
print(f"Point coordinates: {point}")

# Tuple unpacking
x, y = point
print(f"x = {x}, y = {y}")

# Calculate distance from origin
distance = math.sqrt(x**2 + y**2)
print(f"Distance from origin: {distance}\n")

# Define a named tuple for Student
Student = namedtuple('Student', ['name', 'age', 'grade'])

# Create student instances
student1 = Student('Alice', 20, 'A')
student2 = Student('Bob', 22, 'B')
student3 = Student('Charlie', 21, 'A')

# Access data using dot notation
print(f"Student 1: {student1}")
print(f"Name: {student1.name}, Grade: {student1.grade}")

# Can also access by index (like regular tuple)
print(f"Name (by index): {student1[0]}\n")

# Create list of students and sort by grade
students = [student1, student2, student3]
sorted_students = sorted(students, key=lambda s: s.grade)

print("Students sorted by grade:")
for student in sorted_students:
    print(f"  {student.name} - Grade: {student.grade}")

# Demonstrate immutability
# Uncommenting the line below would raise an error:
# student1.name = 'Bob'  # AttributeError: can't set attribute
```

## Explanation

**Regular Tuples:**
Tuples are immutable sequences created with parentheses: `(3, 4)`. Once created, you cannot change their contents.

**Tuple Unpacking:**
`x, y = point` unpacks the tuple into separate variables. This works with any iterable and is very Pythonic.

**Named Tuples:**
A `namedtuple` is a factory function that creates a tuple subclass with named fields. It combines the memory efficiency of tuples with the readability of classes.

**Defining Named Tuples:**
```python
Student = namedtuple('Student', ['name', 'age', 'grade'])
```
- First argument: the typename (class name)
- Second argument: field names as a list

**Accessing Data:**
Named tuples support both:
- Dot notation: `student1.name` (readable)
- Index access: `student1[0]` (like regular tuples)

**Why Use Named Tuples?**
Compared to regular tuples:
- More readable: `student.name` vs `student[0]`
- Self-documenting code
- Still immutable and memory-efficient

Compared to classes:
- Less code to write
- Memory efficient (no `__dict__`)
- Perfect for simple data containers

**Immutability Benefits:**
- Can be used as dictionary keys
- Thread-safe
- Prevents accidental modification
- Can be cached/hashed

**When to Use Tuples vs Lists:**
- Tuples: Fixed collections, heterogeneous data (different types), need immutability
- Lists: Variable-size collections, homogeneous data, need to modify

## Key Concepts

1. **Tuples**: Immutable sequences of values
2. **Tuple Unpacking**: Assigning tuple elements to variables
3. **Named Tuples**: Tuples with named fields for clarity
4. **Immutability**: Cannot change after creation (benefits: hashable, safe)
5. **Memory Efficiency**: Tuples use less memory than lists
6. **Use Cases**: Function returns, dictionary keys, structured data
