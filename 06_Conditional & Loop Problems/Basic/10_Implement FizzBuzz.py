"""
Program: FizzBuzz from 1 to 100
Author: Suraj Prakash
"""

#                                       Method 1

for num in range(1, 101):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


#                                       Method 2

def fizzbuzz(n: int):
    """Return FizzBuzz sequence up to n."""
    output = []
    for num in range(1, n + 1):
        if num % 15 == 0:
            output.append("FizzBuzz")
        elif num % 3 == 0:
            output.append("Fizz")
        elif num % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(num))
    return output


if __name__ == "__main__":
    for line in fizzbuzz(100):
        print(line)
