# Exercise 12: Property Decorators

**Difficulty:** Advanced

## Objective
Use property decorators to create managed attributes with getters, setters, and deleters.

## Requirements
1. Create a `Temperature` class with a private `_celsius` attribute
2. Use `@property` to create a `celsius` getter
3. Use `@celsius.setter` to create a celsius setter with validation (must be >= -273.15)
4. Create a `fahrenheit` property that calculates from celsius
5. Create a `fahrenheit` setter that converts and stores as celsius
6. Add a deleter that resets the temperature
7. Demonstrate read-only properties (getter only, no setter)

## Expected Output
```
Temperature: 25.0°C (77.0°F)
Setting to 100°C
New temperature: 100.0°C (212.0°F)

Setting Fahrenheit to 32°F
Temperature in Celsius: 0.0°C

Trying to set invalid temperature (-300°C):
Error: Temperature cannot be below absolute zero (-273.15°C)

Read-only property (kelvin): 273.15K
```

## Hints
- Use `@property` decorator for getter methods
- Use `@property_name.setter` for setter methods
- Use `@property_name.deleter` for deleter methods
- Private attributes start with `_`
- Properties allow computed values without storing them
- Validation goes in the setter

## Key Concepts
- @property decorator
- Getters and setters
- Data validation
- Computed properties
- Read-only properties
- Encapsulation
