"""
PROGRAM: Fibonacci Using Recursion
DESCRIPTION:
    Returns the nth Fibonacci number using recursion.

LOGIC:
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2)

EXAMPLE:
    fib(10) → 55
"""

def fib(n):
    if n < 0:
        return "Invalid input"
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(10))
