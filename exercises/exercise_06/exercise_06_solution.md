# Exercise 6: Solution

## Code
```python
class Vehicle:
    """Base class for all vehicles."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self):
        return f"Vehicle: {self.year} {self.brand} {self.model}"


class Car(Vehicle):
    """Car class inheriting from Vehicle."""

    def __init__(self, brand, model, year, num_doors):
        # Call parent class constructor
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def describe(self):
        # Override parent method
        return f"Car: {self.year} {self.brand} {self.model}, {self.num_doors} doors"


class Motorcycle(Vehicle):
    """Motorcycle class inheriting from Vehicle."""

    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type

    def describe(self):
        return f"Motorcycle: {self.year} {self.brand} {self.model}, Type: {self.bike_type}"


# Create instances
vehicle = Vehicle("Toyota", "Camry", 2020)
car = Car("Honda", "Accord", 2022, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2021, "Cruiser")

# Call describe methods
print(vehicle.describe())
print(car.describe())
print(motorcycle.describe())
```

## Explanation

**Inheritance Syntax:**
`class Car(Vehicle):` means Car inherits from Vehicle. Car is the child (subclass), Vehicle is the parent (superclass).

**What Does Inheritance Give Us?**
- Car and Motorcycle automatically have access to all Vehicle attributes and methods
- We can add new attributes specific to each subclass
- We can override methods to provide specialized behavior

**The super() Function:**
`super().__init__(brand, model, year)` calls the parent class's `__init__` method. This ensures the parent class is properly initialized before we add child-specific attributes.

Why use `super()`?
- Avoids code duplication
- Maintains the initialization chain
- Required when parent has important setup logic

**Method Overriding:**
Both Car and Motorcycle define their own `describe()` method, which replaces (overrides) the parent's version. When you call `car.describe()`, Python uses the Car version, not the Vehicle version.

**Inheritance Benefits:**
1. **Code Reuse**: Common attributes/methods in one place
2. **Organization**: Clear hierarchy of related classes
3. **Extensibility**: Easy to add new vehicle types
4. **Polymorphism**: All vehicles have a `describe()` method, but behavior differs

**IS-A Relationship:**
Inheritance represents an "IS-A" relationship:
- A Car IS-A Vehicle ✓
- A Motorcycle IS-A Vehicle ✓
- A Car IS-A Motorcycle ✗ (doesn't make sense)

## Key Concepts

1. **Inheritance**: Child classes inherit attributes/methods from parent
2. **super()**: Access parent class methods and constructors
3. **Method Overriding**: Child class replaces parent's method implementation
4. **Code Reuse**: Avoid duplicating common functionality
5. **Class Hierarchy**: Organizing related classes in a tree structure
6. **Polymorphism**: Different classes with same method names but different behaviors
