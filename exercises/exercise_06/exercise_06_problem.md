# Exercise 6: Class Inheritance

**Difficulty:** Intermediate+

## Objective
Create a class hierarchy for different types of vehicles, demonstrating inheritance and method overriding.

## Requirements
1. Create a base `Vehicle` class with `brand`, `model`, and `year` attributes
2. Add a `describe()` method to the Vehicle class
3. Create a `Car` class that inherits from Vehicle and adds `num_doors`
4. Create a `Motorcycle` class that inherits from Vehicle and adds `bike_type`
5. Override the `describe()` method in both subclasses to add specific information
6. Create instances of Car and Motorcycle and call their methods

## Expected Output
```
Vehicle: 2020 Toyota Camry
Car: 2022 Honda Accord, 4 doors
Motorcycle: 2021 Harley-Davidson Street 750, Type: Cruiser
```

## Hints
- Use `class ChildClass(ParentClass):` for inheritance
- Call parent constructor with `super().__init__(...)`
- Override methods by defining them again in the child class
- Use `super().method_name()` to call parent method from child

## Key Concepts
- Inheritance and class hierarchies
- Method overriding
- super() for parent class access
- Code reuse through inheritance
- IS-A relationship
