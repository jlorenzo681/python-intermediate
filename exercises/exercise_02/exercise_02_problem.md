# Exercise 2: Working with Sets

**Difficulty:** Intermediate

## Objective
Create a program that uses sets to analyze two lists of student names and find common students, unique students, and all students.

## Requirements
1. Create two lists of student names (some students should appear in both lists)
2. Convert the lists to sets
3. Find and print students who are in both classes (intersection)
4. Find and print students who are only in class A (difference)
5. Find and print students who are only in class B (difference)
6. Find and print all unique students (union)

## Expected Output
```
Class A: {'Alice', 'Bob', 'Charlie', 'David'}
Class B: {'Charlie', 'David', 'Eve', 'Frank'}
Students in both classes: {'Charlie', 'David'}
Students only in Class A: {'Alice', 'Bob'}
Students only in Class B: {'Eve', 'Frank'}
All students: {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'}
```

## Hints
- Use `set()` to convert a list to a set
- Use `&` or `.intersection()` for common elements
- Use `-` or `.difference()` for elements in one set but not the other
- Use `|` or `.union()` for all unique elements
- Sets automatically remove duplicates

## Key Concepts
- Sets and set operations
- Intersection, difference, and union
- Converting between lists and sets
- Set comprehension
