# Exercise 8: Solution

## Code
```python
import re


# 1. Email validation
def validate_email(email):
    """Validate email address using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


emails = ["user@example.com", "invalid.email", "test@domain.co.uk"]
print("Email Validation:")
for email in emails:
    status = "Valid" if validate_email(email) else "Invalid"
    print(f"  {email} - {status}")


# 2. Extract phone numbers
text = """
Contact us at (555) 123-4567 or 555-987-6543.
You can also try 5551234567.
"""

phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
phones = re.findall(phone_pattern, text)
print("\nPhone Numbers Found:")
for phone in phones:
    print(f"  {phone.strip()}")


# 3. Extract URLs
paragraph = """
Visit our website at https://www.example.com for more info.
Also check out http://test.org for documentation.
"""

url_pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
urls = re.findall(url_pattern, paragraph)
print("\nURLs Found:")
for url in urls:
    print(f"  {url}")


# 4. Parse dates using groups
date_string = "12/25/2023"
date_pattern = r'(\d{2})/(\d{2})/(\d{4})'
match = re.search(date_pattern, date_string)

print("\nDate Parsing:")
if match:
    month, day, year = match.groups()
    print(f"  {date_string} -> Month: {month}, Day: {day}, Year: {year}")
```

## Explanation

**Regular Expressions (Regex):**
Regex is a powerful pattern-matching language for text. It uses special characters to describe patterns.

**Common Regex Patterns:**
- `\d` - any digit (0-9)
- `\w` - any word character (letter, digit, underscore)
- `\s` - any whitespace
- `.` - any character except newline
- `^` - start of string
- `$` - end of string
- `+` - one or more
- `*` - zero or more
- `?` - zero or one (optional)
- `[]` - character class (any one character in brackets)
- `()` - group (for extraction)

**Email Pattern Breakdown:**
```
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
^ - start of string
[a-zA-Z0-9._%+-]+ - one or more valid email characters
@ - literal @ symbol
[a-zA-Z0-9.-]+ - domain name
\. - literal dot (escaped)
[a-zA-Z]{2,} - 2 or more letters (like 'com', 'uk')
$ - end of string
```

**Phone Pattern Breakdown:**
```
\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}
\(? - optional opening parenthesis
\d{3} - exactly 3 digits
\)? - optional closing parenthesis
[-.\s]? - optional separator (dash, dot, or space)
\d{3} - exactly 3 digits
[-.\s]? - optional separator
\d{4} - exactly 4 digits
```

**Re Module Functions:**
- `re.match(pattern, string)` - Match at start of string only
- `re.search(pattern, string)` - Search anywhere in string
- `re.findall(pattern, string)` - Find all matches (returns list)
- `re.sub(pattern, replacement, string)` - Replace matches

**Groups:**
Parentheses `()` create groups that you can extract:
```python
match = re.search(r'(\d{2})/(\d{2})/(\d{4})', '12/25/2023')
month = match.group(1)  # '12'
day = match.group(2)    # '25'
year = match.group(3)   # '2023'
# or: month, day, year = match.groups()
```

**Raw Strings:**
Always use raw strings `r"pattern"` for regex. This prevents Python from interpreting backslashes as escape characters.

**When to Use Regex:**
- ✓ Validation (emails, phones, etc.)
- ✓ Extracting structured data
- ✓ Find and replace with patterns
- ✗ Parsing complex formats (use specialized parsers)
- ✗ When simple string methods work

## Key Concepts

1. **Regular Expressions**: Pattern language for text matching
2. **Metacharacters**: Special characters with meaning (`\d`, `+`, `*`, etc.)
3. **Character Classes**: `[]` for matching sets of characters
4. **Groups**: `()` for capturing parts of matches
5. **Quantifiers**: `+`, `*`, `?`, `{n}` for repetition
6. **re Module**: Python's regex library
