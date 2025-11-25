# Exercise 10: Generators and Yield
# Objective: Create memory-efficient generators using yield

# Hints:
# - Use 'yield' instead of 'return' in generator functions
# - Generators produce values lazily (on demand)
# - Use next(generator) to get next value
# - Generator expression: (x for x in range(10))
# - Generators can only be iterated once
# - Use sys.getsizeof() to check memory usage

# Your code here:

import sys

def fibonacci_generator(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b, a+b

print("First 10 Fibonacci numbers: ")
fibo = fibonacci_generator(10)
print(", ".join(str(x) for x in fibo))

def even_numbers(start, end):
    for x in range(start,end + 1):
        if x % 2 == 0:
            yield x

print("Even numbers from 1 to 20: ")
even = even_numbers(1,20)
print(", ".join(str(x) for x in even))


print("Manual interaction: ")

fibo2 = fibonacci_generator(10)

print(f'Next: {next(fibo2)}')
print(f'Next: {next(fibo2)}')
print(f'Next: {next(fibo2)}')


print(f'Generator expression(squares of evens): ')
squares_gen = (x**2 for x in range(1,11) if x % 2 == 0)
print(", ".join(str(x) for x in squares_gen))


def numb_list(n):
    return [x for x in range(n)]

def numb_generator(n):
    for x in range(n):
        yield x

large_list = numb_list(10000)
large_gen = numb_generator(10000)

list_size = sys.getsizeof(large_list)
gen_size = sys.getsizeof(large_gen)

print(f'\n Memory usage for 10000 numbers: ')
print(f'List: {list_size}')
print(f'Generator: {gen_size}')
print(f'Lists uses {list_size/gen_size} x more memory than generator!')

