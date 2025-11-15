# Exercise 11: Solution

## Code
```python
class Animal:
    """Base class for all animals."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Flyable:
    """Mixin for flying capability."""

    def fly(self):
        return f"{self.name} is flying!"

    def can_fly(self):
        return True


class Swimmable:
    """Mixin for swimming capability."""

    def swim(self):
        return f"{self.name} is swimming!"

    def can_swim(self):
        return True


class Duck(Animal, Flyable, Swimmable):
    """Duck can fly and swim."""

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says Quack!"


class Penguin(Animal, Swimmable):
    """Penguin can only swim, not fly."""

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says Squawk!"

    def fly(self):
        return f"{self.name} cannot fly!"


# Create instances
donald = Duck("Donald")
print(donald.speak())
print(donald.fly())
print(donald.swim())

print()

tux = Penguin("Tux")
print(tux.speak())
print(tux.swim())
print(tux.fly())

print()

# Show Method Resolution Order
print("Duck MRO:", " -> ".join(cls.__name__ for cls in Duck.__mro__))
print("Penguin MRO:", " -> ".join(cls.__name__ for cls in Penguin.__mro__))
```

## Explanation

**Multiple Inheritance:**
A class can inherit from multiple parent classes:
```python
class Duck(Animal, Flyable, Swimmable):
```
Duck inherits from all three parent classes.

**Mixin Classes:**
A mixin is a small class designed to add specific functionality. Flyable and Swimmable are mixins - they're not meant to be instantiated alone, but to be mixed into other classes.

Benefits of mixins:
- Reusable functionality
- Composition over inheritance
- Single responsibility (each mixin does one thing)

**Method Resolution Order (MRO):**
When a method is called, Python searches for it in this order:
1. The class itself
2. Parent classes from left to right
3. Their parent classes, and so on
4. Finally, object base class

For Duck: `Duck -> Animal -> Flyable -> Swimmable -> object`

**The C3 Linearization:**
Python uses C3 linearization algorithm for MRO. It ensures:
- Children come before parents
- Parents maintain the order specified in inheritance
- Each class appears only once

**super() in Multiple Inheritance:**
`super()` doesn't just call the parent class - it calls the **next class in MRO**:

```python
class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name)  # Calls Animal.__init__
```

This follows the MRO chain correctly.

**The Diamond Problem:**
```
    Animal
    /    \
Flyable  Swimmable
    \    /
     Duck
```

If Animal.__init__ is called through both paths, does it run twice? No! Python's MRO ensures each class is visited only once.

**When to Use Multiple Inheritance:**
- ✓ Adding capabilities with mixins
- ✓ Combining orthogonal (independent) features
- ✗ Complex hierarchies (prefer composition)
- ✗ When simpler solutions exist

**Composition vs Inheritance:**
Sometimes composition (has-a) is better than inheritance (is-a):
```python
# Inheritance
class Duck(Animal, Flyable, Swimmable):
    pass

# Composition
class Duck(Animal):
    def __init__(self, name):
        self.flyer = Flyer()
        self.swimmer = Swimmer()
```

Use inheritance for "is-a" relationships, composition for "has-a".

**Checking MRO:**
```python
Duck.__mro__  # Tuple of classes in MRO
Duck.mro()    # List of classes in MRO
```

## Key Concepts

1. **Multiple Inheritance**: Inheriting from multiple parent classes
2. **Mixins**: Small classes that add specific functionality
3. **MRO (Method Resolution Order)**: Order Python searches for methods
4. **C3 Linearization**: Algorithm determining MRO
5. **super()**: Calls next class in MRO, not just parent
6. **Diamond Problem**: How to handle common ancestors
7. **Composition vs Inheritance**: When to use each approach
