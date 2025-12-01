# Exercise 16: CSV File Processing SI

**Difficulty:** Intermediate+

## Objective
Read, process, and write CSV (Comma-Separated Values) files using Python's csv module.

## Requirements
1. Create sample employee data and write it to a CSV file
2. Read the CSV file and display its contents
3. Use DictReader and DictWriter for easier column access
4. Filter data (e.g., employees with salary > threshold)
5. Calculate statistics (average salary, department counts)
6. Write filtered/processed data to a new CSV file
7. Handle CSV files with different delimiters (semicolon, tab)

## Expected Output
```
Writing employees to employees.csv...
Done!

Reading employees from CSV:
ID: 1, Name: Alice Smith, Department: Engineering, Salary: 75000
ID: 2, Name: Bob Johnson, Department: Marketing, Salary: 65000
ID: 3, Name: Charlie Brown, Department: Engineering, Salary: 80000
ID: 4, Name: Diana Prince, Department: HR, Salary: 70000

Statistics:
Average salary: $72,500.00
Department counts: {'Engineering': 2, 'Marketing': 1, 'HR': 1}

High earners (>= $70,000) written to high_earners.csv
```

## Hints
- Import csv module
- Use csv.writer() and csv.reader() for basic operations
- Use csv.DictWriter() and csv.DictReader() for dict-based access
- Always use 'newline=""' when opening CSV files
- Use 'with open()' for safe file handling
- Specify delimiter with delimiter=',' (or ';', '\t', etc.)

## Key Concepts
- CSV file format
- csv module
- DictReader and DictWriter
- File I/O with CSV
- Data filtering and aggregation
- Different delimiters
