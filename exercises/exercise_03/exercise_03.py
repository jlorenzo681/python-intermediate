# Exercise 3: Lambda Functions and Functional Programming
# Objective: Use lambda with map, filter, and sorted

# Hints:
# - Lambda syntax: lambda x: x * 2
# - map() applies a function to each element
# - filter() keeps elements where function returns True
# - sorted(list, key=lambda x: ...) sorts by a custom key
# - Convert map/filter to list using list()

# Your code here:

original_numbers = list(range(1,11))
print(f'Original numbers: {original_numbers}')

square = lambda x: x ** 2
square_map = list(map(square, original_numbers))
print(f'Squared numbers: {square_map}')

even = lambda x: x % 2 == 0
even_filter = list(filter(even, original_numbers))
print(f'Even numbers: {even_filter}')

products = [{
    "name": "Monitor", "price": 150}, {
        "name": "Mouse", "price": 30}, {
            "name": "Keyboard", "price": 25
        }]
sorted_products = sorted(products, key = lambda x: x["price"])
print(f'Products sorted by price:')
for product in sorted_products:
    print(f'{product["name"]} - ${product["price"]}')
