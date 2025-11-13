"""
Program: Multiplication Table
Author: Suraj Prakash
"""

#                   Method 1

n = int(input("Enter a number: "))
print(f"Multiplication table of {n}")

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")

#                   Method 2

def multiplication_table(n: int):
    """Return the multiplication table of n as a list of formatted strings."""
    return [f"{n} * {i} = {n * i}" for i in range(1, 11)]


if __name__ == "__main__":
    for row in multiplication_table(5):
        print(row)

