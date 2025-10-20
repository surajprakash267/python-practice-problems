#✅ 7. Find Common Elements in Two Lists
#M1:                        Using loop

l1 = [2, 5, 7, "a", "n"]
l2 = [3, 2, "n"]
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)


#M2:                                Using list comprehension

l1 = [2, 5, 7, "a", "n"]
l2 = [3, 2, "n"]
common = [x for x in l1 if x in l2]
print(common)


#M3: Using set intersection

l1 = [2, 5, 7, "a", "n"]
l2 = [3, 2, "n"]
print(list(set(l1) & set(l2)))


