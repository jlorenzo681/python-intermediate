# Exercise 24: Data Pipeline with Generators SI

**Difficulty:** Advanced++

## Objective
Build a memory-efficient data processing pipeline using generators, decorators, and functional programming.

## Requirements
1. Create generators to read large CSV files line by line
2. Chain generators to filter, transform, and aggregate data
3. Implement a pipeline decorator for timing and logging
4. Process data without loading entire dataset into memory
5. Calculate statistics on streaming data
6. Demonstrate lazy evaluation benefits
7. Compare memory usage: generator pipeline vs list-based approach

## Expected Features
- Generator-based CSV reader
- Filtering generator (e.g., high-value transactions)
- Transformation generator (e.g., extract specific fields)
- Aggregation using generators
- Pipeline composition
- Memory efficiency demonstration

## Hints
- Use yield for generators
- Chain generators: gen3(gen2(gen1(data)))
- Use decorators for logging/timing
- Generator expressions for simple transformations
- Use itertools for advanced generator operations
- Don't call list() on generators (defeats purpose)

## Key Concepts
- Generator functions
- Generator pipelines
- Lazy evaluation
- Memory efficiency
- Functional composition
- Decorator patterns
