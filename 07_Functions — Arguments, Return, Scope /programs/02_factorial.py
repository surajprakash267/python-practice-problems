"""
PROGRAM: Factorial Using Recursion
DESCRIPTION:
    This program calculates the factorial of a number.
    Factorial(n) = n * (n-1) * (n-2) ... 1

LOGIC:
    - If n < 0 → not allowed
    - If n == 0 or 1 → return 1
    - Else → return n * fact(n-1)

EXAMPLE:
    Input: 5
    Output: 120
"""

def fact(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if num in (0, 1):
        return 1
    return num * fact(num - 1)


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"Factorial of {num} = {fact(num)}")
    except ValueError as e:
        print(e)
