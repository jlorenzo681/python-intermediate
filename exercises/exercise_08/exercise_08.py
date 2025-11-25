# Exercise 8: Regular Expressions
# Objective: Use regex for validation and data extraction

# Hints:
# - Import re module
# - Use raw strings: r"pattern"
# - \d = digit, \w = word char, \s = whitespace
# - + = one or more, * = zero or more, ? = optional
# - () = groups for extraction
# - re.match(), re.search(), re.findall()

# Your code here:

import re

#Email validation

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email)

emails = ["user@example.com", "invalid.email", "test@domain.co.uk"]
print("Email validation: ")
for email in emails:
    status = "Valid" if validate_email(email) else "Invalid"
    print(f'{email} - {status}')


text_phone = "Contact us at (555) 123-4567 or 555-987-6543. You can try 5551234567 too"

phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
phones = re.findall(phone_pattern,text_phone)
print("Phone Numbers Found: ")
for phone in phones:
    print(f'{phone}')


text_paragraph = "Visit our webside: https://www.example.com. Also: http://test.org"
paragraph_pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
paragraph = re.findall(paragraph_pattern,text_paragraph)
print("URLs Found: ")
for parag in paragraph:
    print(f'{parag}')


data_string = "12/25/2023"
data_pattern = r'(\d{2})/(\d{2})/(\d{4})'
match = re.search(data_pattern, data_string)

print("Date Parsing: ")
if match:
     month,day,year = match.groups()
     print(f'{data_string} -> Month:{month}, Day: {day}, Year: {year}')