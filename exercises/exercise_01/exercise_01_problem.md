# Exercise 1: Introduction to Classes

**Difficulty:** Intermediate

## Objective
Create a `Person` class that represents a person with a name and age, and can introduce themselves.

## Requirements
1. Create a class called `Person`
2. The class should have an `__init__` method that accepts `name` and `age` as parameters
3. Create an `introduce()` method that returns a greeting string
4. Create two Person objects and call their `introduce()` methods

## Expected Output
```
Hello, my name is Alice and I am 30 years old.
Hello, my name is Bob and I am 25 years old.
```

## Hints
- Use the `class` keyword to define a class
- The first parameter of any method in a class should be `self`
- Store the name and age as instance variables using `self.name` and `self.age`
- The `__init__` method is called automatically when you create a new object

## Key Concepts
- Classes and objects
- The `__init__` constructor method
- Instance variables and methods
- The `self` parameter
