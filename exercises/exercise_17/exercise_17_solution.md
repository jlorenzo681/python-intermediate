# Exercise 17: Solution

## Code
```python
from datetime import datetime, date, time, timedelta

# 1. Current date and time
now = datetime.now()
today = date.today()
current_time = datetime.now().time()

print(f"Current datetime: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Current date: {today}")
print(f"Current time: {current_time.strftime('%H:%M:%S')}")

# 2. Format dates
print("\nFormatted dates:")
print(now.strftime("%m/%d/%Y"))
print(now.strftime("%B %d, %Y"))
print(now.strftime("%a, %b %d, %Y"))

# 3. Parse dates
date_str = "2024-01-15"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")

# 4. Time deltas
deadline = datetime(2024, 3, 1)
days_until = (deadline - now).days
hours_until = (deadline - now).total_seconds() / 3600

print(f"\nTime delta:")
print(f"Days until deadline: {days_until} days")
print(f"Hours: {int(hours_until)} hours")

# 5. Age calculation
birthdate = date(1998, 6, 15)
age = (today - birthdate).days // 365
print(f"\nAge calculation:")
print(f"Age: {age} years")

# 6. Date arithmetic
print(f"\nDate arithmetic:")
thirty_days_later = today + timedelta(days=30)
print(f"30 days from now: {thirty_days_later}")

# Find previous Monday
days_since_monday = today.weekday()
previous_monday = today - timedelta(days=days_since_monday)
print(f"Previous Monday: {previous_monday}")
```

## Key Concepts
- datetime.now(), date.today()
- strftime() for formatting
- strptime() for parsing
- timedelta for durations
- Date arithmetic
- Format codes (%Y, %m, %d, etc.)
