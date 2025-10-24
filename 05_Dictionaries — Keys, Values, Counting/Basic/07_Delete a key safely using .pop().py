# ✅ 7️⃣ Delete a key safely using .pop()


d = {'a': 1, 'b': 2, 'c': 3}
d.pop('d', None)   # Removes 'b' safely; no error if 'b' not found
print(d)