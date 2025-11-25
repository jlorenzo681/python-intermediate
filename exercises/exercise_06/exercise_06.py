# Exercise 6: Class Inheritance
# Objective: Create a vehicle class hierarchy with inheritance

# Hints:
# - Inherit using: class Child(Parent):
# - Call parent constructor: super().__init__(...)
# - Override methods by redefining them in child class
# - All child classes inherit parent attributes and methods

# Your code here:

class Vehicle():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def describe(self):
        return f'{self.model}: {self.year} {self.brand}'

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand,model,year)
        self.num_doors = num_doors

    def describe(self):
        return f'Car: {self.year} {self.brand} {self.model}, {self.num_doors} doors'
    
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model,year)
        self.bike_type = bike_type

    def describe(self):
        return f'Motorcycle: {self.year} {self.brand} {self.model}, Type: {self.bike_type}'


vehicle = Vehicle("Toyota Camry", "Vehicle", 2020)
car = Car("Honda", "Accord", 2022, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2021, "Cruiser")

print(vehicle.describe())
print(car.describe())
print(motorcycle.describe())

