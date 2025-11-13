"""
Program: Find largest element (without max())
Author: Suraj Prakash
"""

#                                       Method 1

numbers = [1000, 3, 4, 99, 761, 54]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element is:", largest)


#                                       Method 2

def find_largest(lst):
    """Return the largest element in a list."""
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest


if __name__ == "__main__":
    print(find_largest([10, 25, 3, 44, 99, 7]))
