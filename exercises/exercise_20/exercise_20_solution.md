# Exercise 20: Solution

## Code
```python
import sqlite3

# 1. Create database and connect
db_name = 'products.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
print(f"Database created: {db_name}")

# 2. Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    )
''')
conn.commit()
print("Table 'products' created\n")

# 3. Insert data (parameterized queries)
products = [
    ('Laptop', 999.99, 10),
    ('Mouse', 25.50, 50),
    ('Keyboard', 75.00, 30),
    ('Monitor', 299.99, 15)
]

cursor.executemany('INSERT INTO products (name, price, stock) VALUES (?, ?, ?)', products)
conn.commit()
print(f"Inserted {len(products)} products\n")

# 4. Query all products
cursor.execute('SELECT * FROM products')
rows = cursor.fetchall()
print("All products:")
for row in rows:
    print(f"  {row[0]}: {row[1]} - ${row[2]} (Stock: {row[3]})")

# 5. Query with WHERE clause
cursor.execute('SELECT id, name, price FROM products WHERE price < ?', (100,))
cheap_products = cursor.fetchall()
print("\nProducts under $100:")
for product in cheap_products:
    print(f"  {product[0]}: {product[1]} - ${product[2]}")

# 6. Update
cursor.execute('UPDATE products SET price = ? WHERE id = ?', (29.99, 2))
conn.commit()
print("\nUpdated price for product ID 2")

# 7. Delete
cursor.execute('DELETE FROM products WHERE id = ?', (4,))
conn.commit()
print("Deleted product ID 4")

# Final count
cursor.execute('SELECT COUNT(*) FROM products')
count = cursor.fetchone()[0]
print(f"\nFinal product count: {count}")

# Close connection
conn.close()
```

## Key Concepts
- sqlite3.connect() for database connection
- cursor.execute() for SQL commands
- Parameterized queries with ? placeholders
- commit() to save changes
- fetchall(), fetchone() to get results
- CRUD: Create, Read, Update, Delete
- SQL injection prevention with parameters
