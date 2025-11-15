# Exercise 23: Solution

## Code
```python
import sqlite3
from datetime import datetime, timedelta
from typing import List, Optional


class Task:
    """Represents a task with scheduling information."""

    def __init__(self, task_id: Optional[int], title: str, description: str,
                 due_date: datetime, priority: str = "Medium", status: str = "Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def is_overdue(self) -> bool:
        return self.status != "Completed" and self.due_date < datetime.now()

    def __str__(self) -> str:
        return f"[{self.priority}] {self.title} - Due: {self.due_date.strftime('%Y-%m-%d')}"


class TaskScheduler:
    """Manages tasks with SQLite persistence."""

    def __init__(self, db_name: str = 'tasks.db'):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    due_date TEXT NOT NULL,
                    priority TEXT,
                    status TEXT
                )
            ''')

    def add_task(self, task: Task):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO tasks (title, description, due_date, priority, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (task.title, task.description, task.due_date.isoformat(),
                  task.priority, task.status))
            task.task_id = cursor.lastrowid

    def get_all_tasks(self) -> List[Task]:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tasks')
            return [self._row_to_task(row) for row in cursor.fetchall()]

    def get_overdue_tasks(self) -> List[Task]:
        tasks = self.get_all_tasks()
        return [t for t in tasks if t.is_overdue()]

    def complete_task(self, task_id: int):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('UPDATE tasks SET status = ? WHERE id = ?',
                        ('Completed', task_id))

    def _row_to_task(self, row) -> Task:
        task_id, title, desc, due_date, priority, status = row
        due_date = datetime.fromisoformat(due_date)
        return Task(task_id, title, desc, due_date, priority, status)


# Demo
scheduler = TaskScheduler()
task1 = Task(None, "Finish project", "Complete Python exercises",
             datetime.now() + timedelta(days=7), "High")
scheduler.add_task(task1)
print("Task added successfully")

overdue = scheduler.get_overdue_tasks()
print(f"Overdue tasks: {len(overdue)}")
```

## Key Concepts
- SQLite for persistence
- Datetime for due date handling
- OOP design (Task and TaskScheduler)
- Context managers for DB connections
- Filtering and querying
- ISO datetime format
