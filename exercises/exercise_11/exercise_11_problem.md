# Exercise 11: Multiple Inheritance and super()

**Difficulty:** Advanced

## Objective
Create a class hierarchy with multiple inheritance and properly use `super()` to handle the Method Resolution Order (MRO).

## Requirements
1. Create a `Flyable` mixin class with a `fly()` method
2. Create a `Swimmable` mixin class with a `swim()` method
3. Create an `Animal` base class with `name` and `speak()` method
4. Create a `Duck` class that inherits from Animal, Flyable, and Swimmable
5. Create a `Penguin` class that inherits from Animal and Swimmable only
6. Demonstrate the Method Resolution Order (MRO) using `__mro__` or `mro()`
7. Use `super()` correctly in multiple inheritance

## Expected Output
```
Donald says Quack!
Donald is flying!
Donald is swimming!

Tux says Squawk!
Tux is swimming!
Tux cannot fly!

Duck MRO: Duck -> Animal -> Flyable -> Swimmable -> object
Penguin MRO: Penguin -> Animal -> Swimmable -> object
```

## Hints
- Use `super().__init__()` to call parent constructors in order
- MRO determines which parent method is called
- Check MRO with `ClassName.__mro__` or `ClassName.mro()`
- Mixins are small classes that add specific functionality
- Order of inheritance matters: `class Duck(Animal, Flyable, Swimmable)`

## Key Concepts
- Multiple inheritance
- Mixin classes
- Method Resolution Order (MRO)
- super() in complex hierarchies
- Diamond problem
