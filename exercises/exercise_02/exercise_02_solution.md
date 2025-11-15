# Exercise 2: Solution

## Code
```python
# Create two lists of students
class_a = ['Alice', 'Bob', 'Charlie', 'David', 'Alice']  # Note: Alice appears twice
class_b = ['Charlie', 'David', 'Eve', 'Frank']

# Convert to sets (duplicates automatically removed)
set_a = set(class_a)
set_b = set(class_b)

print(f"Class A: {set_a}")
print(f"Class B: {set_b}")

# Find students in both classes (intersection)
both_classes = set_a & set_b  # or set_a.intersection(set_b)
print(f"Students in both classes: {both_classes}")

# Find students only in Class A (difference)
only_a = set_a - set_b  # or set_a.difference(set_b)
print(f"Students only in Class A: {only_a}")

# Find students only in Class B (difference)
only_b = set_b - set_a  # or set_b.difference(set_a)
print(f"Students only in Class B: {only_b}")

# Find all unique students (union)
all_students = set_a | set_b  # or set_a.union(set_b)
print(f"All students: {all_students}")
```

## Explanation

**Sets:**
A set is an unordered collection of unique elements. Unlike lists, sets automatically remove duplicates and don't maintain order.

**Set Creation:**
`set(class_a)` converts the list to a set. Notice how duplicate 'Alice' entries are automatically removed.

**Intersection (`&` or `.intersection()`):**
Finds elements that exist in both sets. Charlie and David are in both classes.

**Difference (`-` or `.difference()`):**
`set_a - set_b` finds elements in set_a that are NOT in set_b. Alice and Bob are only in Class A.

**Union (`|` or `.union()`):**
Combines all unique elements from both sets. This gives us all students across both classes.

**Set Operations Summary:**
- `&` or `.intersection()`: Elements in both sets
- `|` or `.union()`: All unique elements from both sets
- `-` or `.difference()`: Elements in first set but not in second
- `^` or `.symmetric_difference()`: Elements in either set but not both

## Key Concepts

1. **Sets**: Unordered collections of unique elements
2. **Automatic Deduplication**: Sets remove duplicates automatically
3. **Set Operations**: Mathematical operations like intersection, union, difference
4. **Performance**: Sets are optimized for membership testing (very fast)
5. **Immutability**: Can't have duplicate values in a set
