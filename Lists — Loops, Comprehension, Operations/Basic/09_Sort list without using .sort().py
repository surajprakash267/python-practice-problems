#M1:                             Bubble Sort

l1 = [2, 5, 7, 5, 9, 87, 54, 900, 0, 20]

for i in range(len(l1)):
    for j in range(len(l1) - i - 1):
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]

print("Sorted list:", l1)


#M2:                        Using built-in sorted()

l1 = [2, 5, 7, 5, 9, 87, 54, 900, 0, 20]
print("Sorted list:", sorted(l1))
