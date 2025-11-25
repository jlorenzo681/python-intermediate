class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self):
        return f'Vehicle: {self.year} {self.brand} {self.model}'
    
class Car(Vehicle):
    def __init__(self,brand,model,year,num_doors):
        super().__init__(brand,model,year)
        self.num_doors = num_doors

    def describe(self):
        return f'Car: {self.year} {self.brand} {self.model}, {self.num_doors} doors'
    
class Motocycle(Vehicle):
    def __init__(self,brand,model,year,bike_type):
        super().__init__(brand,model,year)
        self.bike_type = bike_type

    def describe(self):
        return f'Motocycle: {self.year} {self.brand} {self.model}, Type: {self.bike_type}'
    

vehicle = Vehicle("Toyota", "Camry", 2020)
car = Car("Honda", "Accord", 2022, 4)
motocycle = Motocycle("Harley-Davidson", "Street 750", 2021, "Cruiser")

print(vehicle.describe())
print(car.describe())
print(motocycle.describe())