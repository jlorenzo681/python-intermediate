# Exercise 13: Context Managers

**Difficulty:** Advanced

## Objective
Create custom context managers using both the class-based approach and the `contextlib` decorator.

## Requirements
1. Create a `FileManager` context manager class that opens and closes files
2. Implement `__enter__` and `__exit__` methods
3. Handle exceptions in `__exit__`
4. Create a `Timer` context manager using `@contextmanager` decorator
5. Create a `DatabaseConnection` context manager that simulates connection handling
6. Demonstrate using `with` statement for automatic resource management
7. Show exception handling within context managers

## Expected Output
```
Using FileManager:
File opened: test.txt
Writing to file...
File closed: test.txt

Using Timer:
Code block took 1.0023 seconds

Using DatabaseConnection:
Connected to database: mydb
Executing query...
Disconnected from database: mydb

Exception handling:
File opened: bad.txt
An error occurred: Division by zero!
File closed: bad.txt (cleanup happened despite error)
```

## Hints
- Implement `__enter__` to return the resource
- Implement `__exit__` to cleanup (takes exception info)
- Return True from `__exit__` to suppress exceptions
- Use `@contextmanager` decorator with `yield`
- `try-finally` in `__exit__` ensures cleanup
- `with open() as f:` is a built-in context manager

## Key Concepts
- Context managers and the `with` statement
- `__enter__` and `__exit__` magic methods
- Resource management
- Exception handling in context managers
- @contextmanager decorator
- Automatic cleanup
