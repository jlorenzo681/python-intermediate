point_coordinates = (3,4)
print(f'Point coordinates: {point_coordinates}')

x,y = point_coordinates
print(f'x = {x}, y = {y}')

import math
distance_origin = math.sqrt(x**2 + y**2)
print(f'Distance from origin = {distance_origin}\n')

from collections import namedtuple

student = namedtuple("Student",["name", "age", "grade"])
student1 = student("Alice", 20, "A")
student2 = student("Charlie", 21, "A")
student3 = student("Bob", 22, "B")

print(f'Student 1: {student1}')
print(f'Name = {student1.name}, Grade: {student1.grade}')
print(f'Name(by index): {student1[0]}\n')

students = [student1, student2, student3]
sorted_students = sorted(students, key = lambda x: x.grade)
print("Students sorted by grade: ")
for student in sorted_students:
    print(f'{student.name} - Grade: {student.grade}')