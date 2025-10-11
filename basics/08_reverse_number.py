#Reverse a number or string

#M1 ::: Using Loop

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)



# M2:::::

num = input("Enter a number: ")
print(num[::-1])


#M3 ::: Using Recursion

def reverse_num(num, rev=0):
    if num == 0:
        return rev
    return reverse_num(num // 10, rev * 10 + num % 10)

num = int(input("Enter a number: "))
print(f"Reversed: {reverse_num(num)}")

