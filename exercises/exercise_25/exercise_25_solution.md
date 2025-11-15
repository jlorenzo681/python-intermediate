# Exercise 25: Solution

## Code
```python
import sqlite3
import json
from datetime import datetime
from typing import List, Optional
from functools import wraps


class InventoryError(Exception):
    """Base exception for inventory errors."""
    pass


class InsufficientStockError(InventoryError):
    """Raised when trying to remove more stock than available."""
    pass


def log_operation(func):
    """Decorator to log all inventory operations."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {func.__name__} called")
        result = func(*args, **kwargs)
        return result
    return wrapper


class Product:
    """Represents a product with validation."""

    def __init__(self, product_id: Optional[int], name: str, category: str,
                 price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.category = category
        self._price = 0
        self._stock = 0
        self.price = price  # Use setter for validation
        self.stock = stock

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int):
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value

    @property
    def total_value(self) -> float:
        return self.price * self.stock

    def __str__(self) -> str:
        return f"{self.name} ({self.category}) - ${self.price} [Stock: {self.stock}]"

    def __repr__(self) -> str:
        return f"Product({self.product_id}, {self.name!r}, {self.category!r}, {self.price}, {self.stock})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Product) and self.product_id == other.product_id


class InventoryManager:
    """Manages inventory with SQLite persistence."""

    def __init__(self, db_name: str = 'inventory.db'):
        self.db_name = db_name
        self._create_tables()

    def _create_tables(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    change INTEGER,
                    timestamp TEXT,
                    FOREIGN KEY (product_id) REFERENCES products(id)
                )
            ''')

    @log_operation
    def add_product(self, product: Product):
        """Add a new product."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO products (name, category, price, stock)
                VALUES (?, ?, ?, ?)
            ''', (product.name, product.category, product.price, product.stock))
            product.product_id = cursor.lastrowid

    @log_operation
    def update_stock(self, product_id: int, change: int):
        """Update stock level (positive to add, negative to remove)."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT stock FROM products WHERE id = ?', (product_id,))
            row = cursor.fetchone()

            if not row:
                raise InventoryError(f"Product {product_id} not found")

            current_stock = row[0]
            new_stock = current_stock + change

            if new_stock < 0:
                raise InsufficientStockError(
                    f"Cannot remove {abs(change)} items. Only {current_stock} in stock."
                )

            cursor.execute('UPDATE products SET stock = ? WHERE id = ?',
                          (new_stock, product_id))

            # Log transaction
            cursor.execute('''
                INSERT INTO transactions (product_id, change, timestamp)
                VALUES (?, ?, ?)
            ''', (product_id, change, datetime.now().isoformat()))

    def get_low_stock_products(self, threshold: int = 10) -> List[Product]:
        """Get products with stock below threshold."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products WHERE stock < ?', (threshold,))
            return [self._row_to_product(row) for row in cursor.fetchall()]

    def search_by_category(self, category: str) -> List[Product]:
        """Find all products in a category."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products WHERE category = ?', (category,))
            return [self._row_to_product(row) for row in cursor.fetchall()]

    def get_total_inventory_value(self) -> float:
        """Calculate total value of all inventory."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT price, stock FROM products')
            return sum(price * stock for price, stock in cursor.fetchall())

    def export_to_json(self, filename: str):
        """Export inventory to JSON file."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products')
            products = [self._row_to_dict(row) for row in cursor.fetchall()]

        with open(filename, 'w') as f:
            json.dump(products, f, indent=2)

    def _row_to_product(self, row) -> Product:
        product_id, name, category, price, stock = row
        return Product(product_id, name, category, price, stock)

    def _row_to_dict(self, row) -> dict:
        product_id, name, category, price, stock = row
        return {
            'id': product_id,
            'name': name,
            'category': category,
            'price': price,
            'stock': stock
        }


# Demo
if __name__ == '__main__':
    manager = InventoryManager()

    # Add products
    laptop = Product(None, "Laptop", "Electronics", 999.99, 15)
    mouse = Product(None, "Mouse", "Electronics", 25.50, 5)

    manager.add_product(laptop)
    manager.add_product(mouse)

    # Check low stock
    low_stock = manager.get_low_stock_products(threshold=10)
    print(f"\nLow stock items: {len(low_stock)}")

    # Update stock
    try:
        manager.update_stock(1, -5)  # Remove 5 laptops
        print("Stock updated")
    except InsufficientStockError as e:
        print(f"Error: {e}")

    # Total value
    total_value = manager.get_total_inventory_value()
    print(f"\nTotal inventory value: ${total_value:,.2f}")

    # Export
    manager.export_to_json('inventory_backup.json')
    print("Inventory exported to JSON")
```

## Key Concepts
- Comprehensive OOP (Product, InventoryManager)
- Property decorators with validation
- SQLite database with foreign keys
- Custom exceptions
- Logging decorator
- Magic methods (__str__, __repr__, __eq__)
- Transaction history
- JSON import/export
- Search and filtering
- Statistics calculation
- Error handling
