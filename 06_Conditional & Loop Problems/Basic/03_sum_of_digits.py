"""
Program: Sum of digits of a number
Author: Suraj Prakash
"""
#                   Method 1

n = int(input("Enter the number: "))
digit_sum = 0
while n > 0:
    digit = n % 10 # get the last digit
    digit_sum = digit_sum + digit
    n = n // 10
print(f"The sum of digits is {digit_sum}")

#                   Method 2

def sum_of_digits(n: int):
    """Return the sum of digits of a number."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


if __name__ == "__main__":
    print(sum_of_digits(12345))
