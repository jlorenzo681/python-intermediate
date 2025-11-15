# Exercise 24: Data Pipeline with Generators
# Objective: Build memory-efficient data processing pipeline

# Hints:
# - Use generators (yield) for each pipeline stage
# - Chain generators: gen3(gen2(gen1(data)))
# - Don't convert to list (defeats lazy evaluation)
# - Each generator processes one item at a time
# - Use functools.wraps for decorators
# - Compare memory: generator vs list approach

# Your code here:
