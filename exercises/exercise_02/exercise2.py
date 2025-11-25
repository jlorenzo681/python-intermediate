class_a = ["Alice", "Bob", "Charlie", "David"]
class_b = ["Charlie", "David", "Eve", "Frank"]

set_a = set(class_a)
set_b = set(class_b) 

print(f'Class A: {set_a}')
print(f'Class B: {set_b}')

both_classes = set_a & set_b
print(f'Students in both classes: {both_classes}')

only_a = set_a - set_b
print(f'Students only in class A: {only_a}')
only_b = set_b - set_a
print(f'Students only in class B: {only_b}')

all_classes_unique = set_a | set_b
print(f'All students: {all_classes_unique}')