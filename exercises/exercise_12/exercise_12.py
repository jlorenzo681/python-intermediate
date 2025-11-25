# Exercise 12: Property Decorators
# Objective: Use @property for managed attributes with validation

# Hints:
# - @property for getter
# - @property_name.setter for setter
# - @property_name.deleter for deleter
# - Private attributes: _attribute_name
# - Validate in setter, compute in getter
# - Read-only: property with no setter

# Your code here:

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
    @property
    def kelvin(self):
        return self._celsius + 273.15
    @celsius.deleter
    def celsius(self):
        print("Resetting temperature to 0°C")
        self._celsius = 0
    def __str__(self):
        return (f'{self._celsius}ºC ({self.fahrenheit}ºF)')

temperature = Temperature(25) 
print(f'Temperature: {temperature}')      
print(f'Setting to 100ºC')
temperature.celsius = 100
print(f'New temperature: {temperature}')

print(f'\nSetting Fahrenheit to 32ºF')
temperature.fahrenheit = 32
print(f'Temperature in Celsius: {temperature}')

print("\nTrying to set invalid temperature (-300°C):")
try:
    temperature.celsius = -300
except ValueError as e:
    print(f'Error: {e}')

temperature.celsius = 0
print(f'\nRead-only property (kelvin):{temperature.kelvin}K')
