# Exercise 1: Introduction to Classes
# Objective: Create a Person class with name, age, and an introduce method

# Hints:
# - Use 'class ClassName:' to define a class
# - The __init__ method should accept self, name, and age
# - Store name and age as self.name and self.age
# - The introduce method should return a formatted string

# Your code here:

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f'Hello, my name is {self.name} and I am {self.age} year old.')


alice = Person("Alice", 30)
bob = Person("Bob",25)

alice.greeting()
bob.greeting()

        
    