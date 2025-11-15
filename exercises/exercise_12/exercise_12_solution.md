# Exercise 12: Solution

## Code
```python
class Temperature:
    """Temperature class with property decorators."""

    def __init__(self, celsius=0):
        self._celsius = celsius  # Private attribute

    @property
    def celsius(self):
        """Getter for celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Computed property: Fahrenheit from Celsius."""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter: Convert Fahrenheit to Celsius."""
        self.celsius = (value - 32) * 5/9

    @property
    def kelvin(self):
        """Read-only property: Kelvin from Celsius."""
        return self._celsius + 273.15

    @celsius.deleter
    def celsius(self):
        """Deleter: Reset temperature."""
        print("Resetting temperature to 0°C")
        self._celsius = 0

    def __str__(self):
        return f"{self._celsius}°C ({self.fahrenheit}°F)"


# Create temperature object
temp = Temperature(25)
print(f"Temperature: {temp}")

# Use property setter
print("\nSetting to 100°C")
temp.celsius = 100
print(f"New temperature: {temp}")

# Use computed property
print("\nSetting Fahrenheit to 32°F")
temp.fahrenheit = 32
print(f"Temperature in Celsius: {temp.celsius}°C")

# Validation
print("\nTrying to set invalid temperature (-300°C):")
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")

# Read-only property
temp.celsius = 0
print(f"\nRead-only property (kelvin): {temp.kelvin}K")

# Trying to set read-only property would raise AttributeError
# temp.kelvin = 300  # Uncommenting this would raise an error
```

## Explanation

**Why Use Properties?**
Properties allow you to add behavior to attribute access without changing the interface. You can:
- Validate values before setting
- Calculate values on-the-fly
- Make attributes read-only
- Add logging or debugging
- Change internal representation without breaking code

**The @property Decorator:**
```python
@property
def celsius(self):
    return self._celsius
```

This makes `celsius` look like an attribute but actually call a method:
```python
temp.celsius  # Calls the getter method, no ()
```

**The @property.setter Decorator:**
```python
@celsius.setter
def celsius(self, value):
    if value < -273.15:
        raise ValueError(...)
    self._celsius = value
```

Now you can assign to it:
```python
temp.celsius = 25  # Calls the setter method
```

**Validation in Setters:**
The setter is the perfect place for validation. Any attempt to set invalid values raises an exception.

**Computed Properties:**
The `fahrenheit` property doesn't have its own storage - it's calculated from celsius:
```python
@property
def fahrenheit(self):
    return self._celsius * 9/5 + 32
```

This is more efficient than storing both values and keeping them in sync.

**Read-Only Properties:**
Define a getter but no setter:
```python
@property
def kelvin(self):
    return self._celsius + 273.15
```

Trying to assign raises `AttributeError`:
```python
temp.kelvin = 300  # AttributeError: can't set attribute
```

**The @property.deleter:**
```python
@celsius.deleter
def celsius(self):
    self._celsius = 0
```

Called with `del temp.celsius`.

**Private Attributes Convention:**
`_celsius` (single underscore) signals "internal use" - it's a convention, not enforced. Python doesn't have true private attributes (though `__name` triggers name mangling).

**Old Style vs Properties:**
```python
# Old style (Java-like)
def get_celsius(self):
    return self._celsius

def set_celsius(self, value):
    self._celsius = value

temp.set_celsius(25)
x = temp.get_celsius()

# Pythonic with properties
@property
def celsius(self):
    return self._celsius

temp.celsius = 25
x = temp.celsius
```

Properties are more Pythonic and cleaner.

## Key Concepts

1. **@property**: Make methods look like attributes
2. **Getters**: Control how attributes are accessed
3. **Setters**: Control how attributes are modified
4. **Validation**: Check values before storing
5. **Computed Properties**: Calculate values on demand
6. **Read-Only**: Properties with getter but no setter
7. **Encapsulation**: Hide internal representation
