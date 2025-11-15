# Exercise 19: Solution

## Code
```python
from collections import Counter, defaultdict, deque

# 1. Counter
print("Counter Examples:")
letters = list("hello world")
letter_count = Counter(letters)
print(f"Letter counts: {dict(letter_count.most_common()[:4])}")
print(f"Most common: {letter_count.most_common(2)}")

# 2. defaultdict
print("\ndefaultdict Examples:")
students = [
    ('Alice', 'A'),
    ('Bob', 'B'),
    ('Charlie', 'A'),
    ('Diana', 'C')
]

grade_groups = defaultdict(list)
for name, grade in students:
    grade_groups[grade].append(name)

print("Students by grade:")
for grade in sorted(grade_groups.keys()):
    print(f"  {grade}: {grade_groups[grade]}")

# 3. deque
print("\ndeque Examples:")
queue = deque([1, 2, 3, 4, 5])
print(f"Queue: {queue}")

# Pop from both ends
right = queue.pop()
print(f"Popped from right: {right}")
left = queue.popleft()
print(f"Popped from left: {left}")
print(f"Remaining: {queue}")

# Rotate
queue.rotate(1)  # Rotate right
print(f"\nRotating: {queue}")

# 4. Performance comparison
print("\ndeque is much faster for popleft() than list")
```

## Key Concepts
- Counter: Efficient counting
- defaultdict: Auto-initialize missing keys
- deque: O(1) operations on both ends
- Specialized containers for specific use cases
