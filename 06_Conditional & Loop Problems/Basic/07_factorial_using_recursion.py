"""
Program: Factorial using recursion with input validation
Author: Suraj Prakash
"""

#                   Method 1

def facto(n):
    if n in (0, 1):
        return 1
    return n * facto(n - 1)

try:
    user_input = input("Enter number to calculate factorial: ")
    num = int(user_input)

    if num < 0:
        print("Factorial not defined for negative numbers.")
    else:
        print(f"Factorial of {num} is {facto(num)}")

except ValueError:
    print(f"Invalid input '{user_input}'. Please enter a valid number.")



#                   Method 2

def factorial(n: int):
    """Return the factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))
