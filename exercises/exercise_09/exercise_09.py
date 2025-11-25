# Exercise 9: Working with JSON Data
# Objective: Read, write, and manipulate JSON data

# Hints:
# - Import json module
# - Write to file: json.dump(data, file, indent=4)
# - Read from file: json.load(file)
# - Always use 'with open()' for file operations
# - Handle IOError and json.JSONDecodeError
# - Filter with list comprehensions

# Your code here:

import json

products = [{"name": "Laptop", "price": 999.99, "quantity": 5, "category": "electronics"},
            {"name": "Mouse", "price": 25.50, "quantity": 50 , "category": "electronics"},
            {"name": "Desk", "price": 299.00, "quantity": 10, "category": "furniture"}
]

print("Original Products: ")
for product in products:
    print(product)


filename = "inventory_json"
with open(filename, "w") as f:
    json.dump(products, f, indent=4)
print(f'Products save to {filename}')


with open(filename, "r") as f:
    loaded_products = json.load(f)

electronics = [p for p in loaded_products if p["category"] == "electronics"]
print("Electronics products: ")
for product in electronics:
    print(f' {product["name"]}: ${product["price"]} ({product["quantity"]}) in stock')

total_value = sum(p["price"] * p["quantity"] for p in loaded_products)
print(f"Total inventory value: ${total_value:.2f}")

for product in loaded_products:
    if product["name"] == "Mouse":
        product["quantity"] = 45
        print(f'Update Mousse quantity to {product["quantity"]}')
        break

with open(filename, "w") as f:
    json.dump(loaded_products,f, indent=4)
    print(f'Products updated in {filename}')