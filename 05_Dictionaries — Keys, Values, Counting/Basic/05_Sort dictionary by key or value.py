#✅ 5️⃣                          Sort dictionary by key or value


#                                Sort by key:

d = {'b': 2, 'a': 5, 'c': 1}
sorted_by_key = dict(sorted(d.items()))
print(sorted_by_key)

#                                Sort by value:


sorted_by_val = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_by_val)

