# Exercise 2: Working with Sets
# Objective: Use set operations to analyze two lists of students

# Hints:
# - Convert lists to sets using set()
# - Use & for intersection (common elements)
# - Use - for difference (elements in first but not second)
# - Use | for union (all unique elements)

# Your code here:
class_a = ["Alice", "Bob", "Charlie", "David"]
class_b = ["Charlie", "David", "Eve", "Frank"]

set_a = set(class_a)
set_b = set(class_b)

print(f'Class A: {set_a}')
print(f'Class B: {set_b}')

both_classes = set_a & set_b
print(f'Students in both classes: {both_classes}')

one_set_a = set_a - set_b
print(f'Students only in Class A: {one_set_a}')

one_set_b = set_b - set_a
print(f'Students only in Class B: {one_set_b}')

all_students = set_a | set_b
print(f'All students: {all_students}')