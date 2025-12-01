# Exercise 20: SQLite Database Operations NO

**Difficulty:** Advanced

## Objective
Use Python's sqlite3 module to create databases, tables, and perform CRUD operations.

## Requirements
1. Create a SQLite database and a products table
2. Insert multiple product records
3. Query data with SELECT statements
4. Update existing records
5. Delete records
6. Use parameterized queries to prevent SQL injection
7. Handle database connections properly with context managers

## Expected Output
```
Database created: products.db
Table 'products' created

Inserted 4 products

All products:
  1: Laptop - $999.99 (Stock: 10)
  2: Mouse - $25.50 (Stock: 50)
  3: Keyboard - $75.00 (Stock: 30)
  4: Monitor - $299.99 (Stock: 15)

Products under $100:
  2: Mouse - $25.50
  3: Keyboard - $75.00

Updated price for product ID 2
Deleted product ID 4

Final product count: 3
```

## Hints
- import sqlite3
- conn = sqlite3.connect('database.db')
- cursor = conn.cursor()
- Use ? placeholders for parameters
- conn.commit() to save changes
- conn.close() or use with statement
- cursor.execute() for single query
- cursor.executemany() for bulk insert

## Key Concepts
- SQLite database
- SQL CRUD operations
- Parameterized queries
- Database connections and cursors
- SQL injection prevention
- Context managers for databases
