# Exercise 9: Solution

## Code
```python
import json


# 1. Create product data
products = [
    {'name': 'Laptop', 'price': 999.99, 'quantity': 5, 'category': 'Electronics'},
    {'name': 'Mouse', 'price': 25.50, 'quantity': 50, 'category': 'Electronics'},
    {'name': 'Desk', 'price': 299.00, 'quantity': 10, 'category': 'Furniture'},
    {'name': 'Chair', 'price': 199.00, 'quantity': 15, 'category': 'Furniture'}
]

print("Original Products:")
for product in products[:3]:  # Show first 3
    print(product)


# 2. Write to JSON file
filename = 'inventory.json'
try:
    with open(filename, 'w') as f:
        json.dump(products, f, indent=4)
    print(f"\nProducts saved to {filename}")
except IOError as e:
    print(f"Error writing to file: {e}")


# 3. Read from JSON file
try:
    with open(filename, 'r') as f:
        loaded_products = json.load(f)
except (IOError, json.JSONDecodeError) as e:
    print(f"Error reading file: {e}")
    loaded_products = []


# 4. Filter products by category
electronics = [p for p in loaded_products if p['category'] == 'Electronics']
print("\nElectronics products:")
for product in electronics:
    print(f"  {product['name']}: ${product['price']} ({product['quantity']} in stock)")


# 5. Calculate total inventory value
total_value = sum(p['price'] * p['quantity'] for p in loaded_products)
print(f"\nTotal inventory value: ${total_value:.2f}")


# 6. Update a product and save
for product in loaded_products:
    if product['name'] == 'Mouse':
        product['quantity'] = 45
        print(f"\nUpdated Mouse quantity to {product['quantity']}")
        break

# Save updated data
with open(filename, 'w') as f:
    json.dump(loaded_products, f, indent=4)
print(f"Products updated in {filename}")
```

## Explanation

**JSON (JavaScript Object Notation):**
JSON is a lightweight data format for storing and exchanging data. It's human-readable and language-independent.

**JSON Data Types:**
- Objects: `{}` (like Python dicts)
- Arrays: `[]` (like Python lists)
- Strings: `"text"`
- Numbers: `42`, `3.14`
- Booleans: `true`, `false`
- Null: `null`

**Python to JSON Mapping:**
- dict → JSON object
- list/tuple → JSON array
- str → JSON string
- int/float → JSON number
- True/False → true/false
- None → null

**Writing JSON:**
```python
with open('file.json', 'w') as f:
    json.dump(data, f, indent=4)
```
- `json.dump()` - write to file
- `indent=4` - pretty print with 4-space indentation
- Always use context manager (`with`)

**Reading JSON:**
```python
with open('file.json', 'r') as f:
    data = json.load(f)
```
- `json.load()` - read from file
- Returns Python objects (dict, list, etc.)

**JSON Strings vs Files:**
- `json.dumps(data)` - convert to JSON string
- `json.loads(string)` - parse JSON string
- `json.dump(data, file)` - write to file
- `json.load(file)` - read from file

**List Comprehension with Filtering:**
```python
electronics = [p for p in products if p['category'] == 'Electronics']
```
Creates a new list with only products matching the condition.

**Generator Expression for Sum:**
```python
total = sum(p['price'] * p['quantity'] for p in products)
```
Efficiently calculates total without creating intermediate list.

**Error Handling:**
- `IOError` - file read/write errors
- `json.JSONDecodeError` - invalid JSON format
- Always handle these when working with files

**When to Use JSON:**
- ✓ Configuration files
- ✓ API data exchange
- ✓ Simple data persistence
- ✓ Cross-language data sharing
- ✗ Binary data (use pickle or binary formats)
- ✗ Complex Python objects (use pickle)

## Key Concepts

1. **JSON Format**: Lightweight data interchange format
2. **Serialization**: Converting Python objects to JSON
3. **Deserialization**: Converting JSON to Python objects
4. **json.dump/load**: File operations
5. **json.dumps/loads**: String operations
6. **Pretty Printing**: indent parameter for readability
7. **Context Managers**: `with open()` for safe file handling
