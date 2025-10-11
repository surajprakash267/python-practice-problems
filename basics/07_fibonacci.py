 #Generate Fibonacci series up to n terms

"""
Logic:
Each term = sum of previous two terms
Example: 0, 1, 1, 2, 3, 5, 8, 13 …
🧠 Tip:
Start with 0, 1 and keep adding the last two numbers.

"""


n = int(input("Enter how many Fibonacci numbers: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


#M2 : Using Recursion
"""
Logic:
Calls itself for n-1 and n-2.
Elegant but slower for large n (no memoization).

"""
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Enter number of terms: "))
for i in range(n):
    print(fib(i), end=" ")

#M3 : One-liner (list comprehension)

n = int(input("Enter number of terms: "))
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for i in range(2, n)]
print(fib[:n])

