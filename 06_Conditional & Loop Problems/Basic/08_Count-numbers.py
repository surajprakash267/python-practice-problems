"""
Program: Count positive, negative and zero numbers in a list
Author: Suraj Prakash
"""
#                                       Method 1

li = [2, 4, -1, 0, -3, 0, 7, -9, 0, 44]

positive = 0
negative = 0
zero_numbers = 0

for i in li:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zero_numbers += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero_numbers)


#                                       Method 2

def count_numbers(lst):
    """Return counts of positive, negative, and zero values."""
    pos = neg = zero = 0
    for num in lst:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    return pos, neg, zero


if __name__ == "__main__":
    print(count_numbers([2, -1, 0, 4, -3, 0]))

