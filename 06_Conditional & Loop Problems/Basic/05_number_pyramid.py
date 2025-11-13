"""
Program: Number Pyramid Pattern
Author: Suraj Prakash
"""

#                   Method 1

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


#                   Method 2

def number_pyramid(rows: int):
    """Return a number pyramid pattern."""
    return [" ".join(str(j) for j in range(1, i + 1)) for i in range(1, rows + 1)]


if __name__ == "__main__":
    for line in number_pyramid(5):
        print(line)
