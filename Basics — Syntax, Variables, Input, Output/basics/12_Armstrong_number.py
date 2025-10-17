#M1 : Using Loop

"""
Logic:
Extract each digit (% 10), raise it to power n, and sum.
Compare with the original number.

"""

num = int(input("Enter a number: "))
n = len(str(num))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** n
    temp //= 10

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


#M2 :  Using Recursion

def armstrong_sum(n, temp):
    if temp == 0:
        return 0
    digit = temp % 10
    return (digit ** n) + armstrong_sum(n, temp // 10)

num = int(input("Enter a number: "))
n = len(str(num))
print("Armstrong" if num == armstrong_sum(n, num) else "Not Armstrong")


#M3 :  One-liner

num = int(input("Enter: "))
n = len(str(num))
print("Armstrong" if num == sum(int(d)**n for d in str(num)) else "Not Armstrong")

