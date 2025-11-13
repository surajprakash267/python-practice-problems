"""
Program: Prime numbers from 1 to 100
Author: Suraj Prakash
"""

#                   Method 1

print("Prime numbers between 1 and 100:")

for num in range(1, 101):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)


#                   Method 2

def primes_in_range(start: int, end: int):
    """Return all prime numbers between start and end."""
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes


if __name__ == "__main__":
    print(primes_in_range(1, 100))


#                           Method 3


print("\nPrime numbers in the range of 1 to 100:")

for num in range(1, 101):
    if num > 1:
        # Check for factors from 2 up to (num - 1)
        for i in range(2, num):
            if (num % i) == 0:
                # If 'i' divides 'num' evenly, it's not prime. Break the inner loop.
                break
            # The 'else' here would be wrong; we must let the loop finish to confirm primality.
        else:
            # This 'else' belongs to the 'for i...' loop.
            # It runs only if the inner loop completed without hitting a 'break'.
            print(num)

