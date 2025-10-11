#.    Check if a number is prime

"""
Logic:
Prime number = only divisible by 1 and itself.

🧠 Tip:
Loop from 2 → num-1, and check if any divides evenly.
"""

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")


#M2 : Using Recursion

def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

num = int(input("Enter: "))
print("Prime" if is_prime(num) else "Not Prime")


#M3:  Using loop

num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


#M4 : One-liner (any + generator)

num = int(input("Enter: "))
print("Prime" if num > 1 and not any(num % i == 0 for i in range(2, int(num ** 0.5) + 1)) else "Not Prime")




