
a, b, c = 23, 34, 10

# Method 1
print("Largest:", max(a, b, c))

# Method 2
if a >= b and a >= c:
    print("A is largest")
elif b >= a and b >= c:
    print("B is largest")
else:
    print("C is largest")
