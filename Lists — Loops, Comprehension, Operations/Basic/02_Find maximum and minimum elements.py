#                   Find Maximum and Minimum Elements
#               M1:         Using max() and min()

l1 = [2, 40, 8, -1, 0]
print(f"Maximum element: {max(l1)}")
print(f"Minimum element: {min(l1)}")

#                       M2: Using sorting

l1 = [2, 40, 8, -1, 0]
l1.sort()
print(f"Minimum element: {l1[0]}")
print(f"Maximum element: {l1[-1]}")

#M3: Using sort(reverse=True)

l1 = [2, 40, 8, -1, 0]
l1.sort(reverse=True)
print(f"Maximum element: {l1[0]}")
print(f"Minimum element: {l1[-1]}")
