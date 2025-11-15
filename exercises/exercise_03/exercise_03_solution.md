# Exercise 3: Solution

## Code
```python
# Create a list of numbers
numbers = list(range(1, 11))
print(f"Original numbers: {numbers}")

# Use map with lambda to square each number
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")

# Use filter with lambda to get only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Create list of product dictionaries
products = [
    {'name': 'Monitor', 'price': 150},
    {'name': 'Keyboard', 'price': 25},
    {'name': 'Mouse', 'price': 30}
]

# Sort products by price using lambda
sorted_products = sorted(products, key=lambda x: x['price'])
print("Products sorted by price:")
for product in sorted_products:
    print(f"  {product['name']} - ${product['price']}")
```

## Explanation

**Lambda Functions:**
A lambda is a small anonymous function defined with the syntax `lambda parameters: expression`. They're useful for simple, one-time operations.

**map() Function:**
`map(lambda x: x ** 2, numbers)` applies the lambda function to each element in numbers. The lambda takes each number `x` and returns `x ** 2`. The result is a map object, which we convert to a list.

**filter() Function:**
`filter(lambda x: x % 2 == 0, numbers)` keeps only elements where the lambda returns True. Here, `x % 2 == 0` is True for even numbers, so only evens pass through.

**sorted() with key:**
The `key` parameter accepts a function that extracts a comparison key from each element. `lambda x: x['price']` tells sorted to compare dictionaries based on their 'price' value.

**Why Use Lambdas?**
Lambdas are concise for simple operations. Compare:
```python
# With lambda
squared = map(lambda x: x ** 2, numbers)

# Without lambda (requires defining a function)
def square(x):
    return x ** 2
squared = map(square, numbers)
```

For simple operations, lambdas are cleaner. For complex logic, define a named function.

## Key Concepts

1. **Lambda Functions**: Anonymous, inline functions for simple operations
2. **map()**: Applies a function to every element in an iterable
3. **filter()**: Selects elements where a function returns True
4. **sorted() with key**: Custom sorting using a key extraction function
5. **Functional Programming**: Treating functions as first-class objects
6. **Higher-Order Functions**: Functions that accept or return other functions
