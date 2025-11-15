# Exercise 8: Regular Expressions

**Difficulty:** Intermediate+

## Objective
Use regular expressions to validate and extract information from text data.

## Requirements
1. Validate email addresses using regex
2. Extract phone numbers from text in different formats
3. Find and extract all URLs from a paragraph
4. Use regex groups to parse date strings (MM/DD/YYYY format)
5. Demonstrate common regex patterns: `\d`, `\w`, `+`, `*`, `?`, `[]`, `()`

## Expected Output
```
Email Validation:
  user@example.com - Valid
  invalid.email - Invalid
  test@domain.co.uk - Valid

Phone Numbers Found:
  (555) 123-4567
  555-987-6543
  5551234567

URLs Found:
  https://www.example.com
  http://test.org

Date Parsing:
  12/25/2023 -> Month: 12, Day: 25, Year: 2023
```

## Hints
- Import re module: `import re`
- `re.match()` - matches at start of string
- `re.search()` - searches anywhere in string
- `re.findall()` - finds all matches
- Use raw strings for regex: `r"pattern"`
- Groups: Use `()` and access with `.group(1)`, `.group(2)`, etc.

## Key Concepts
- Regular expression patterns
- Pattern matching and searching
- Regex groups and extraction
- Common regex metacharacters
- Validation with regex
