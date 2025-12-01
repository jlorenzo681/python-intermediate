# Exercise 21: Contact Management System NO

**Difficulty:** Advanced++

## Objective
Build a complete contact management system using OOP, JSON persistence, and error handling.

## Requirements
1. Create a `Contact` class with name, email, phone, and category
2. Create a `ContactManager` class to manage contacts
3. Implement add, search, update, and delete operations
4. Save/load contacts to/from JSON file
5. Use custom exceptions for error handling
6. Implement data validation (email format, phone format)
7. Support filtering by category and searching by name
8. Add proper docstrings and type hints

## Expected Features
- Add new contacts with validation
- Search contacts by name (case-insensitive)
- Update contact information
- Delete contacts
- List all contacts or filter by category
- Persistent storage with JSON
- Custom exceptions for validation errors
- Context manager for file operations

## Hints
- Use @property for validated attributes
- Use regex for email/phone validation
- Use json module for persistence
- Implement __str__ and __repr__ for Contact
- Use list comprehensions for filtering
- Handle FileNotFoundError for new databases

## Key Concepts
- OOP design
- Data validation
- JSON persistence
- Custom exceptions
- Search and filter operations
- File I/O
