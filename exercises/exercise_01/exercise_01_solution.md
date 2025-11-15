# Exercise 1: Solution

## Code
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Call methods
print(person1.introduce())
print(person2.introduce())
```

## Explanation

**Class Definition:**
The `class Person:` statement defines a new class. A class is a blueprint for creating objects (instances).

**The `__init__` Method:**
This is a special method called a constructor. It's automatically called when you create a new object. The parameters `name` and `age` are stored as instance variables using `self.name` and `self.age`.

**The `self` Parameter:**
Every instance method must have `self` as its first parameter. It refers to the specific instance of the class and allows you to access instance variables and other methods.

**Instance Variables:**
`self.name` and `self.age` are instance variables - they belong to each specific object. Each Person object has its own name and age.

**Creating Objects:**
`Person("Alice", 30)` creates a new Person object. Python automatically calls `__init__` with these arguments.

**Method Calls:**
`person1.introduce()` calls the `introduce` method on the person1 object. Python automatically passes person1 as the `self` parameter.

## Key Concepts

1. **Classes**: Templates for creating objects that bundle data and functionality together
2. **Objects/Instances**: Specific realizations of a class
3. **Constructor (`__init__`)**: Special method for initializing new objects
4. **Instance Variables**: Data that belongs to each object
5. **Instance Methods**: Functions that operate on object data
6. **self**: Reference to the current instance
