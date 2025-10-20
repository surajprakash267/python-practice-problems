# ✅ 5. Flatten a Nested List → [1, [2, 3], [4]] → [1, 2, 3, 4]
# M1: Using loop

l1 = [1, [2, 3], [4]]
flat = []
for i in l1:
    if type(i) == list:
        for j in i:
            flat.append(j)
    else:
        flat.append(i)
print(flat)


#M2:            Using list comprehension

l1 = [1, [2, 3], [4]]
flat = [x for i in l1 for x in (i if isinstance(i, list) else [i])]
print(flat)

#M3:            Using recursion (for deeper nesting)


def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result


print(flatten([1, [2, [3, 4]], [5]]))

