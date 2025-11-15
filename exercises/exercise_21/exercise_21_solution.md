# Exercise 21: Solution

## Code
```python
import json
import re
from typing import List, Optional


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


class Contact:
    """Represents a contact with validation."""

    def __init__(self, name: str, email: str, phone: str, category: str = "Personal"):
        self.name = name
        self.email = email
        self.phone = phone
        self.category = category

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise ValidationError(f"Invalid email: {value}")
        self._email = value

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'category': self.category
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Contact':
        return cls(**data)

    def __str__(self) -> str:
        return f"{self.name} ({self.category}) - {self.email}, {self.phone}"


class ContactManager:
    """Manages contacts with persistence."""

    def __init__(self, filename: str = 'contacts.json'):
        self.filename = filename
        self.contacts: List[Contact] = []
        self.load()

    def add(self, contact: Contact):
        self.contacts.append(contact)
        self.save()

    def search(self, name: str) -> List[Contact]:
        return [c for c in self.contacts if name.lower() in c.name.lower()]

    def delete(self, name: str) -> bool:
        original_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.name != name]
        if len(self.contacts) < original_count:
            self.save()
            return True
        return False

    def filter_by_category(self, category: str) -> List[Contact]:
        return [c for c in self.contacts if c.category == category]

    def save(self):
        with open(self.filename, 'w') as f:
            data = [c.to_dict() for c in self.contacts]
            json.dump(data, f, indent=2)

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.contacts = [Contact.from_dict(c) for c in data]
        except FileNotFoundError:
            self.contacts = []


# Demo
if __name__ == '__main__':
    manager = ContactManager()

    # Add contacts
    try:
        manager.add(Contact("Alice Smith", "alice@example.com", "555-1234", "Work"))
        manager.add(Contact("Bob Jones", "bob@example.com", "555-5678", "Personal"))
        print("Contacts added successfully")
    except ValidationError as e:
        print(f"Error: {e}")

    # Search
    results = manager.search("alice")
    print(f"\nSearch results: {[str(c) for c in results]}")

    # Filter
    work_contacts = manager.filter_by_category("Work")
    print(f"\nWork contacts: {len(work_contacts)}")
```

## Key Concepts
- OOP with Contact and ContactManager classes
- Property decorators for validation
- JSON serialization/deserialization
- Custom exceptions
- Type hints
- List comprehensions for filtering
- File persistence
