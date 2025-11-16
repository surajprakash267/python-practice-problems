"""
PROGRAM: map(), filter(), reduce() Examples
DESCRIPTION:
    Demonstrates functional programming in Python.

FUNCTIONS:
    map()    → applies function to each element
    filter() → selects elements by condition
    reduce() → reduces list to a single value

EXAMPLE:
    Numbers = [1,2,3,4,5]
    Map → squares
    Filter → evens
    Reduce → sum
"""

from functools import reduce

nums = [1, 2, 3, 4, 5]

mapped = list(map(lambda x: x * x, nums))
filtered = list(filter(lambda x: x % 2 == 0, nums))
reduced = reduce(lambda a, b: a + b, nums)

if __name__ == "__main__":
    print("Squares:", mapped)
    print("Evens:", filtered)
    print("Sum:", reduced)
