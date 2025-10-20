l1 = [2, 5, 7, 5, 9, 87, 54, 900, 0, 20]
even = []
odd = []

for i in l1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")
