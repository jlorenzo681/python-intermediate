# Exercise 23: Task Scheduler with SQLite NO

**Difficulty:** Advanced++

## Objective
Build a task scheduling system with SQLite persistence, datetime handling, and OOP.

## Requirements
1. Create Task class with title, description, due_date, priority, status
2. Store tasks in SQLite database
3. Add, update, complete, and delete tasks
4. Query tasks by status, priority, or due date
5. Find overdue tasks
6. Sort tasks by due date or priority
7. Use context managers for database connections
8. Implement proper error handling

## Expected Features
- Create and manage tasks
- Set due dates and priorities (High, Medium, Low)
- Mark tasks as complete
- Find overdue tasks
- Filter by status or priority
- Automatic datetime handling
- Persistent storage

## Hints
- Store dates as ISO format strings in SQLite
- Convert strings to datetime objects when reading
- Use timedelta to find overdue tasks
- Create indexes for better query performance
- Use parameterized queries
- Implement __str__ for Task display

## Key Concepts
- SQLite database operations
- Datetime manipulation
- OOP design
- CRUD operations
- Data filtering and sorting
- Context managers
