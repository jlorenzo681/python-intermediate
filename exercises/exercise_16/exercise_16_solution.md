# Exercise 16: Solution

## Code
```python
import csv
from collections import Counter


# Sample data
employees = [
    {'id': '1', 'name': 'Alice Smith', 'department': 'Engineering', 'salary': '75000'},
    {'id': '2', 'name': 'Bob Johnson', 'department': 'Marketing', 'salary': '65000'},
    {'id': '3', 'name': 'Charlie Brown', 'department': 'Engineering', 'salary': '80000'},
    {'id': '4', 'name': 'Diana Prince', 'department': 'HR', 'salary': '70000'}
]

# 1. Write to CSV using DictWriter
filename = 'employees.csv'
print(f"Writing employees to {filename}...")

with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['id', 'name', 'department', 'salary']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Write column headers
    writer.writerows(employees)  # Write all rows

print("Done!\n")

# 2. Read from CSV using DictReader
print("Reading employees from CSV:")
with open(filename, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    employee_list = []
    for row in reader:
        print(f"ID: {row['id']}, Name: {row['name']}, "
              f"Department: {row['department']}, Salary: {row['salary']}")
        employee_list.append(row)

# 3. Calculate statistics
print("\nStatistics:")
salaries = [int(emp['salary']) for emp in employee_list]
avg_salary = sum(salaries) / len(salaries)
print(f"Average salary: ${avg_salary:,.2f}")

departments = [emp['department'] for emp in employee_list]
dept_counts = dict(Counter(departments))
print(f"Department counts: {dept_counts}")

# 4. Filter and write to new CSV
threshold = 70000
high_earners = [emp for emp in employee_list if int(emp['salary']) >= threshold]

output_file = 'high_earners.csv'
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['id', 'name', 'department', 'salary']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(high_earners)

print(f"\nHigh earners (>= ${threshold:,}) written to {output_file}")
```

## Explanation

**CSV Format:**
CSV (Comma-Separated Values) is a simple text format for tabular data:
```
id,name,department,salary
1,Alice Smith,Engineering,75000
2,Bob Johnson,Marketing,65000
```

**csv Module:**
Python's built-in csv module handles CSV reading/writing correctly (handles quotes, commas in values, etc.).

**DictReader:**
```python
reader = csv.DictReader(csvfile)
for row in reader:
    print(row['name'])  # Access by column name
```

Benefits:
- Access columns by name (more readable)
- Automatically parses header row
- Returns OrderedDict for each row

**DictWriter:**
```python
writer = csv.DictWriter(csvfile, fieldnames=['id', 'name'])
writer.writeheader()  # Write column headers
writer.writerow({'id': '1', 'name': 'Alice'})
```

**Important: newline=''**
Always use `newline=''` when opening CSV files:
```python
with open('file.csv', 'w', newline='') as f:
    ...
```

Without it, you might get extra blank lines on Windows.

**Basic Reader/Writer:**
For simpler cases without column names:
```python
# Writing
writer = csv.writer(csvfile)
writer.writerow(['Alice', 'Engineering', 75000])

# Reading
reader = csv.reader(csvfile)
for row in reader:
    print(row[0], row[1])  # Access by index
```

**Different Delimiters:**
CSV files can use different separators:
```python
# Semicolon-separated
writer = csv.writer(csvfile, delimiter=';')

# Tab-separated (TSV)
writer = csv.writer(csvfile, delimiter='\t')
```

**Handling Special Characters:**
The csv module automatically handles:
- Commas in values: `"Smith, John"`
- Quotes in values: `"He said ""hello"""`
- Newlines in values

**Common Patterns:**

**Read all rows:**
```python
with open('file.csv') as f:
    reader = csv.DictReader(f)
    data = list(reader)  # Load all into memory
```

**Process row by row (memory efficient):**
```python
with open('file.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        process(row)  # Process one at a time
```

**Filter and write:**
```python
with open('input.csv') as fin, open('output.csv', 'w', newline='') as fout:
    reader = csv.DictReader(fin)
    writer = csv.DictWriter(fout, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        if condition(row):
            writer.writerow(row)
```

**Error Handling:**
```python
try:
    with open('file.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                salary = int(row['salary'])
            except (KeyError, ValueError) as e:
                print(f"Error processing row: {e}")
                continue
except FileNotFoundError:
    print("File not found!")
```

**When to Use CSV:**
- ✓ Tabular data
- ✓ Data exchange between systems
- ✓ Export from spreadsheets
- ✓ Simple, portable format
- ✗ Complex nested data (use JSON)
- ✗ Binary data (use pickle or binary formats)
- ✗ Very large files (consider pandas or databases)

## Key Concepts

1. **CSV Format**: Text format for tabular data
2. **csv Module**: Built-in module for CSV operations
3. **DictReader/DictWriter**: Dict-based CSV operations
4. **Fieldnames**: Column names for DictWriter
5. **Delimiters**: Different separators (comma, semicolon, tab)
6. **newline=''**: Required for correct CSV file handling
7. **File I/O**: Always use context managers (`with`)
