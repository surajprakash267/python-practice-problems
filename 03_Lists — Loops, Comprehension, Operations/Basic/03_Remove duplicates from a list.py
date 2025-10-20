#                       ✅ 3. Remove Duplicates from a List
#M1: Using a loop

l1 = [2, 4, 6, 7, "s", 2, 7, "s", "t", 2, 4, 6, 7]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)


#M2: Using set()

l1 = [2, 4, 6, 7, "s", 2, 7, "s", "t", 2, 4]
l2 = list(set(l1))
print(l2)

#(Note: set does not preserve order)