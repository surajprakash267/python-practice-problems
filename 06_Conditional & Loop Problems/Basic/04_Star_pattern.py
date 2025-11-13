"""
Program: Left-aligned star pattern
Author: Suraj Prakash
"""
#                   Method 1

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)

#                   Method 2

def star_pattern(rows: int):
    """Return a list representing a left-aligned star pattern."""
    return ["*" * i for i in range(1, rows + 1)]


if __name__ == "__main__":
    for line in star_pattern(4):
        print(line)
