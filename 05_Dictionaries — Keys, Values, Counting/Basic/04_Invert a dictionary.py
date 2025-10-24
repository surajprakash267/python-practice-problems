#✅ 4️⃣ Invert a dictionary ({'a':1,'b':2} → {1:'a',2:'b'})


d = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in d.items()}
print(inverted)


#⚠️ Works only if values are unique and hashable.