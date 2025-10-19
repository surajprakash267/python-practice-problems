#✅                      4. Merge Two Lists Element-wise
#M1: Using + operator

l1 = [2, 4, 6, 7, "s"]
l2 = [1, 5, 8, 0, "i"]
print(f"Merged list: {l1 + l2}")

#M2: Using list comprehension (pair-wise merge)

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
merged = [(x, y) for x, y in zip(l1, l2)]
print(merged)   # [(1, 'a'), (2, 'b'), (3, 'c')]
