l1 = {2, 5, 7, 9, 87, 54, 900, 0, 20}
print(l1)
print(len(l1))

# 🟢 If l1 were a list, you could also do:

print(len(set(l1)))  # counts unique items


# Bonus challenge for practice:::::

# Remove duplicates from a list but keep the original order
l1 = [2, 5, 7, 5, 9, 87, 54, 900, 0, 20]
result = []
for i in l1:
    if i not in result:
        result.append(i)
print(result)
