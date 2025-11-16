"""
PROGRAM: Sum of Variable Number of Arguments (*args)
DESCRIPTION:
    Demonstrates the use of *args to accept unlimited arguments.

LOGIC:
    - Initialize sum = 0
    - Loop through each argument
    - Add to sum

EXAMPLE:
    sum_all(1, 2, 3) → 6
    sum_all(100) → 100
"""

def sum_all(*args):
    result = 0
    for num in args:
        result += num
    return result


if __name__ == "__main__":
    print(sum_all(1, 2, 3))
    print(sum_all(5, 10, 15, 20))
    print(sum_all(100))
