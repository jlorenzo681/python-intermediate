# Exercise 5: Tuples and Named Tuples
# Objective: Work with tuples and named tuples for structured data

# Hints:
# - Create tuple: point = (x, y)
# - Unpack tuple: x, y = point
# - Import namedtuple: from collections import namedtuple
# - Define namedtuple: Student = namedtuple('Student', ['field1', 'field2'])
# - Access fields: student.name or student[0]
# - Tuples are immutable!

# Your code here:

from collections import namedtuple
import math

point = (3, 4)
print(f'Point coordinates: {point}')

x,y = point
print(f'x = {x}, y = {y}')

distance = math.sqrt(x**2 + y**2)
print(f'Distance from origin = {distance}')

Student = namedtuple("Student",["name", "age", "grade"])

Student1 = Student("Alice", 20, "A")
Student2 = Student("Charlie", 21, "A")
Student3 = Student("Bob", 22, "B")

print(f'\nStudent 1: {Student1}')
print(f'Name: {Student1.name}, Grade: {Student1.grade}')
print(f'Name(by index): {Student1[0]}')

print(f'\nStudent sorted by grade: ')

students = [Student1, Student2, Student3]
sorted_students = sorted(students, key= lambda x: x.grade)
for student in sorted_students:
    print(f'{student.name} - Grade: {student.grade}')