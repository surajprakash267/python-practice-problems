"""
Program: Numbers divisible by 3 and 5 in a range
Author: Suraj Prakash
"""
#                   Method 1

def divisible_by_3_and_5(start: int, end: int):
    """Return numbers divisible by both 3 and 5 between start and end."""
    return [i for i in range(start, end + 1) if i % 3 == 0 and i % 5 == 0]


if __name__ == "__main__":
    print(divisible_by_3_and_5(1, 50))


#                   Method 2

l = []

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        l.append(i)

print("Numbers divisible by both 3 and 5:", l)
