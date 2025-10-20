# M1 : Factorial of a number using a loop

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"Factorial of {n} is {fact}")


# M2 : Using recursion

"""
Logic:
Function calls itself until n becomes 1.
n! = n × (n-1)!
Base case (n == 0 or 1) stops recursion.

"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} = {factorial(num)}")

# M3 : One-liner using Lambda

"""
Logic:
reduce repeatedly applies the inner lambda to multiply values.
One-liner shows understanding of higher-order functions.

"""

from functools import reduce
num = int(input("Enter a number: "))
fact = (lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1))(num)
print(f"Factorial of {num} = {fact}")

