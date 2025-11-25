# Exercise 11: Multiple Inheritance and super()
# Objective: Use multiple inheritance with mixins and understand MRO

# Hints:
# - Multiple inheritance: class Child(Parent1, Parent2, Parent3)
# - Create mixin classes for specific capabilities (Flyable, Swimmable)
# - Use super().__init__() to call parent constructors
# - Check MRO with ClassName.__mro__
# - Order of inheritance matters!

# Your code here:

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "some sound"


class Flyable:
    def fly(self):
        return f'{self.name} is flying!'


class Swimmable:
    def swim(self):
        return f'{self.name} is swimming!'


class Duck(Animal, Flyable, Swimmable):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        return f'{self.name} says Quack!'
    

class Penguin(Animal, Swimmable):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return f'{self.name} says Squawk!'
    def fly(self):
        return f'{self.name} cannot fly!'
    

donald = Duck("Donald")
print(donald.speak())
print(donald.fly())
print(donald.swim())

tux = Penguin("Tux")
print(tux.speak())
print(tux.swim())
print(tux.fly())

print("Duck MRO:", "->".join(cls.__name__ for cls in Duck.__mro__))
print("Penguin MRO:", "->".join(cls.__name__ for cls in Penguin.__mro__))