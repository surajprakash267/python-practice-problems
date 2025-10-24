#Q.              Count occurrences of each element in a list → {1:2,2:3}

"""
✅ 1️⃣ Count occurrences of each element in a list
Goal: {element: count}

"""
#✔️ Correct & Simple version:

l1 = [2, 5, 7, 5, 9, 87, 54, 900, 0, 20]

mod_data = {}
for i in l1:
    if i in mod_data:
        mod_data[i] += 1
    else:
        mod_data[i] = 1

print(f"The required data is : {mod_data}")



# 🔹 Shorter (using dict.get()):

mod_data = {}
for i in l1:
    mod_data[i] = mod_data.get(i, 0) + 1
print(f"The required data is : {mod_data}")

#🔹 Shortest (using collections.Counter):

from collections import Counter
print(Counter(l1))


