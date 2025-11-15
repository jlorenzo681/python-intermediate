# Exercise 24: Solution

## Code
```python
import csv
import time
from functools import wraps
from typing import Iterator, Dict


def timer_decorator(func):
    """Decorator to time generator creation."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} initialized in {time.time() - start:.4f}s")
        return result
    return wrapper


@timer_decorator
def read_csv_lazy(filename: str) -> Iterator[Dict]:
    """Lazy CSV reader using generator."""
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def filter_by_amount(rows: Iterator[Dict], min_amount: float) -> Iterator[Dict]:
    """Filter transactions above threshold."""
    for row in rows:
        if float(row.get('amount', 0)) >= min_amount:
            yield row


def extract_fields(rows: Iterator[Dict], *fields) -> Iterator[Dict]:
    """Extract specific fields from each row."""
    for row in rows:
        yield {field: row.get(field) for field in fields}


def transform_amount(rows: Iterator[Dict]) -> Iterator[Dict]:
    """Convert amount to float."""
    for row in rows:
        row['amount'] = float(row['amount'])
        yield row


def aggregate_by_category(rows: Iterator[Dict]) -> Dict[str, float]:
    """Aggregate amounts by category."""
    totals = {}
    for row in rows:
        category = row.get('category', 'Unknown')
        amount = row.get('amount', 0)
        totals[category] = totals.get(category, 0) + amount
    return totals


# Demo pipeline
def process_transactions(filename: str):
    """Process transactions using generator pipeline."""

    # Build pipeline (lazy - no processing yet!)
    pipeline = read_csv_lazy(filename)
    pipeline = filter_by_amount(pipeline, 100.0)
    pipeline = transform_amount(pipeline)

    # Only now does processing start (when we iterate)
    count = 0
    total = 0
    for transaction in pipeline:
        count += 1
        total += transaction['amount']

    print(f"\nProcessed {count} high-value transactions")
    print(f"Total amount: ${total:,.2f}")


# Compare with list approach
def process_with_lists(filename: str):
    """Non-lazy approach (loads everything)."""
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        all_data = list(reader)  # Load all into memory

    filtered = [r for r in all_data if float(r['amount']) >= 100]
    # Process filtered data...


# Generator pipeline is memory-efficient:
# - Processes one item at a time
# - No intermediate lists
# - Can handle files larger than RAM
```

## Key Concepts
- Generator pipelines
- Lazy evaluation (no processing until iteration)
- Memory efficiency
- Generator composition
- Streaming data processing
- Chaining generators
