# Exercise 9: Working with JSON Data

**Difficulty:** Intermediate+

## Objective
Read, write, and manipulate JSON data representing a product inventory.

## Requirements
1. Create a list of product dictionaries with name, price, quantity, and category
2. Write the products to a JSON file with proper formatting
3. Read the JSON file back into Python
4. Filter products by category
5. Calculate total inventory value
6. Update a product's quantity and save back to file
7. Handle potential JSON errors

## Expected Output
```
Original Products:
{'name': 'Laptop', 'price': 999.99, 'quantity': 5, 'category': 'Electronics'}
{'name': 'Mouse', 'price': 25.50, 'quantity': 50, 'category': 'Electronics'}
{'name': 'Desk', 'price': 299.00, 'quantity': 10, 'category': 'Furniture'}

Products saved to inventory.json

Electronics products:
  Laptop: $999.99 (5 in stock)
  Mouse: $25.50 (50 in stock)

Total inventory value: $8769.95

Updated Mouse quantity to 45
Products updated in inventory.json
```

## Hints
- Import json module: `import json`
- Write JSON: `json.dump(data, file, indent=4)`
- Read JSON: `json.load(file)`
- Convert to JSON string: `json.dumps(data)`
- Parse JSON string: `json.loads(string)`
- Always use `with open()` for file handling

## Key Concepts
- JSON format and structure
- Serialization and deserialization
- File I/O with context managers
- Data filtering and aggregation
- Error handling with JSON
