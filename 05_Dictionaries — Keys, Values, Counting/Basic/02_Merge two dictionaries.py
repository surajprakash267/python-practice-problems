#✅ 2️⃣ Merge two dictionaries
#                                               M1 — Using Unpacking

l1 = {"car": 2, "bus": 4}
l2 = {"cart": 5, "rat": 6}
merged = {**l1, **l2}
print(merged)

#                                      M2 — Using Union Operator (Python 3.9+)

merged = l1 | l2
print(merged)

#                                           M3 — Using update()

l1.update(l2)
print(l1)

# {'car': 2, 'bus': 4, 'cart': 5, 'rat': 6}
# {'car': 2, 'bus': 4, 'cart': 5, 'rat': 6}
# {'car': 2, 'bus': 4, 'cart': 5, 'rat': 6}