# Exercise 19: Collections Module

**Difficulty:** Advanced

## Objective
Use specialized data structures from the collections module: Counter, defaultdict, deque, and namedtuple.

## Requirements
1. Use Counter to count occurrences in a list
2. Find most common elements with Counter
3. Use defaultdict to group data by category
4. Use deque for efficient queue operations (append/pop from both ends)
5. Compare performance of list vs deque for queue operations
6. Demonstrate OrderedDict (maintains insertion order)

## Expected Output
```
Counter Examples:
Letter counts: {'l': 3, 'o': 2, 'h': 1, 'e': 1}
Most common: [('l', 3), ('o', 2)]

defaultdict Examples:
Students by grade:
  A: ['Alice', 'Charlie']
  B: ['Bob']
  C: ['Diana']

deque Examples:
Queue: deque([1, 2, 3, 4, 5])
Popped from right: 5
Popped from left: 1
Remaining: deque([2, 3, 4])

Rotating: deque([4, 2, 3])
```

## Hints
- from collections import Counter, defaultdict, deque
- Counter(list) counts occurrences
- Counter.most_common(n) returns top n
- defaultdict(list) creates list for missing keys
- deque.append(), deque.appendleft()
- deque.pop(), deque.popleft()

## Key Concepts
- Counter for counting
- defaultdict for automatic defaults
- deque for double-ended queues
- Specialized containers
- Performance characteristics
