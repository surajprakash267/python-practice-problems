#.    M1: Using loop

l1 = [2, 308, 34, 103]
l2 = []
for i in l1:
    if i % 2 == 0:
        l2.append(i)
print(l2)

# M2: Using list comprehension

l1 = [2, 308, 34, 103]
l2 = [x for x in l1 if x % 2 == 0]
print(l2)
