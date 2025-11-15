# Exercise 17: Working with Datetime

**Difficulty:** Intermediate+

## Objective
Use Python's datetime module to work with dates, times, and time deltas.

## Requirements
1. Get current date and time
2. Create specific dates and parse date strings
3. Format dates in different ways (strftime)
4. Parse strings to dates (strptime)
5. Calculate time differences (timedelta)
6. Work with time zones (aware vs naive datetimes)
7. Calculate ages, business days, and date arithmetic

## Expected Output
```
Current datetime: 2024-01-15 14:30:45
Current date: 2024-01-15
Current time: 14:30:45

Formatted dates:
01/15/2024
January 15, 2024
Mon, Jan 15, 2024

Time delta:
Days until deadline: 45 days
Hours: 1080 hours

Age calculation:
Age: 25 years

Date arithmetic:
30 days from now: 2024-02-14
Previous Monday: 2024-01-08
```

## Hints
- from datetime import datetime, date, time, timedelta
- datetime.now() for current datetime
- datetime.strptime(string, format) to parse
- datetime.strftime(format) to format
- Use timedelta for date arithmetic
- %Y, %m, %d, %H, %M, %S are common format codes

## Key Concepts
- datetime module
- Date and time objects
- Formatting and parsing
- Time deltas
- Date arithmetic
- Time zones
