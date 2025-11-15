# Exercise 5: Tuples and Named Tuples

**Difficulty:** Intermediate

## Objective
Learn to work with tuples and named tuples by creating a program that manages coordinate points and student records.

## Requirements
1. Create regular tuples to represent 2D coordinates (x, y)
2. Demonstrate tuple unpacking with coordinates
3. Use the `namedtuple` from collections to create a `Student` type
4. Create several Student instances with name, age, and grade
5. Access student data using both dot notation and indexing
6. Show that tuples are immutable (trying to modify raises an error)

## Expected Output
```
Point coordinates: (3, 4)
x = 3, y = 4
Distance from origin: 5.0

Student 1: Student(name='Alice', age=20, grade='A')
Name: Alice, Grade: A
Name (by index): Alice

Students sorted by grade:
  Alice - Grade: A
  Charlie - Grade: A
  Bob - Grade: B
```

## Hints
- Regular tuples: `point = (x, y)`
- Tuple unpacking: `x, y = point`
- Import namedtuple: `from collections import namedtuple`
- Define namedtuple: `Student = namedtuple('Student', ['name', 'age', 'grade'])`
- Access by name: `student.name` or by index: `student[0]`
- Use `sorted()` with a key to sort namedtuples

## Key Concepts
- Tuples as immutable sequences
- Tuple unpacking
- Named tuples for structured data
- Immutability benefits
- When to use tuples vs lists
