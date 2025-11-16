"""
PROGRAM: Lambda to Find Maximum of Two Numbers
DESCRIPTION:
    Demonstrates a lambda with conditional expression.

LOGIC:
    lambda a, b: a if a > b else b

EXAMPLE:
    find_max(10, 20) → 20
"""

find_max = lambda a, b: a if a > b else b

if __name__ == "__main__":
    print(find_max(10, 20))
