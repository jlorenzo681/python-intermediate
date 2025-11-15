# Exercise 13: Solution

## Code
```python
from contextlib import contextmanager
import time


# Class-based context manager
class FileManager:
    """Context manager for file operations."""

    def __init__(self, filename, mode='w'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Called when entering 'with' block."""
        print(f"File opened: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block."""
        if self.file:
            self.file.close()
            print(f"File closed: {self.filename}")
        # Return False to propagate exceptions, True to suppress
        return False


# Function-based context manager using decorator
@contextmanager
def timer():
    """Context manager to time code execution."""
    start_time = time.time()
    try:
        yield  # This is where the 'with' block code runs
    finally:
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Code block took {elapsed:.4f} seconds")


@contextmanager
def database_connection(db_name):
    """Context manager simulating database connection."""
    # Setup (like __enter__)
    print(f"Connected to database: {db_name}")
    connection = {"db": db_name, "connected": True}

    try:
        yield connection  # Provide resource to with block
    finally:
        # Cleanup (like __exit__)
        connection["connected"] = False
        print(f"Disconnected from database: {db_name}")


# Test FileManager
print("Using FileManager:")
with FileManager("test.txt", "w") as f:
    print("Writing to file...")
    f.write("Hello, Context Managers!")

print("\nUsing Timer:")
with timer():
    time.sleep(1)

print("\nUsing DatabaseConnection:")
with database_connection("mydb") as conn:
    print("Executing query...")
    # Simulate database operations

# Exception handling
print("\nException handling:")
try:
    with FileManager("bad.txt", "w") as f:
        print("Writing data...")
        x = 1 / 0  # Intentional error
except ZeroDivisionError:
    print("An error occurred: Division by zero!")
    print("File closed: bad.txt (cleanup happened despite error)")
```

## Explanation

**What is a Context Manager?**
A context manager is an object that defines the runtime context for a `with` statement. It ensures setup and cleanup code is executed, even if errors occur.

**The `with` Statement:**
```python
with context_manager as variable:
    # code block
```

Equivalent to:
```python
variable = context_manager.__enter__()
try:
    # code block
finally:
    context_manager.__exit__()
```

The `finally` ensures cleanup **always** happens.

**Class-Based Context Managers:**
Implement two magic methods:

**`__enter__(self)`:**
- Called when entering the `with` block
- Does setup (open file, connect to database, etc.)
- Returns the resource (file object, connection, etc.)

**`__exit__(self, exc_type, exc_val, exc_tb)`:**
- Called when exiting the `with` block
- Does cleanup (close file, disconnect, etc.)
- Receives exception info if one occurred:
  - `exc_type`: Exception class (or None)
  - `exc_val`: Exception instance (or None)
  - `exc_tb`: Traceback (or None)
- Return `True` to suppress exception, `False` to propagate

**Function-Based Context Managers:**
Use `@contextmanager` decorator:

```python
@contextmanager
def my_context():
    # Setup code
    resource = acquire_resource()
    try:
        yield resource  # Provide resource to with block
    finally:
        # Cleanup code
        release_resource()
```

- Code before `yield` = `__enter__`
- `yield` value = what gets assigned with `as`
- Code after `yield` (in `finally`) = `__exit__`

**Why Use Context Managers?**

1. **Guaranteed Cleanup:** Even if exceptions occur, cleanup runs
2. **Cleaner Code:** No need for explicit try-finally blocks
3. **Resource Management:** Files, locks, connections, etc.
4. **Readability:** Clear scope of resource usage

**Common Built-in Context Managers:**
- `open()`: File handling
- `threading.Lock()`: Thread synchronization
- `decimal.localcontext()`: Decimal precision settings
- Many database libraries: Connection management

**Exception Handling:**
```python
def __exit__(self, exc_type, exc_val, exc_tb):
    cleanup()
    if exc_type is not None:
        # An exception occurred
        print(f"Exception: {exc_val}")
        return True  # Suppress exception
    return False  # Propagate exception
```

**Best Practices:**
1. Always use `try-finally` in function-based context managers
2. Close resources in `__exit__` even if exceptions occur
3. Return `False` from `__exit__` unless you have good reason to suppress
4. Use context managers for resource management (files, locks, connections)

**When to Use Each Style:**
- **Class-based**: Complex state, reusable, multiple methods
- **Function-based**: Simple, one-off, less boilerplate

## Key Concepts

1. **Context Managers**: Objects managing resource setup/cleanup
2. **with Statement**: Syntax for using context managers
3. **__enter__**: Setup method, returns resource
4. **__exit__**: Cleanup method, receives exception info
5. **@contextmanager**: Decorator for function-based context managers
6. **Guaranteed Cleanup**: Cleanup happens even with exceptions
7. **Resource Management**: Files, locks, connections, etc.
