Method	Description	Example
1. .items()	- Returns a view object with key–value pairs as tuples.	d.items() → dict_items([('a',1), ('b',2)])
2. .fromkeys() - 	Creates a new dictionary from given keys and a common value.	dict.fromkeys(['a','b','c'], 0) → {'a':0,'b':0,'c':0}
3. .values() - Returns a view object with all values.	d.values() → dict_values([1,2])
4. .keys() - Returns a view object with all keys.	d.keys() → dict_keys(['a','b'])
5. .update() - Updates dictionary with another dictionary or key-value pairs.	d.update({'c':3})
6. .get() -	Returns value of a key safely (no error if key missing).	d.get('a', 'not found')
7. .pop() -	Removes and returns value of a given key.	d.pop('a')
8. .popitem() -	Removes and returns last inserted (key, value) pair.	d.popitem()
9. .clear() -	Removes all items from the dictionary.	d.clear() → {}

**Examples : **

# Create a sample dictionary
d = {'a': 1, 'b': 2, 'c': 3}

print("Original dictionary:", d)

# 1️⃣ keys()
print("\n1. Keys:", d.keys())

# 2️⃣ values()
print("2. Values:", d.values())

# 3️⃣ items()
print("3. Items:", d.items())

# 4️⃣ get()
print("4. Get existing key:", d.get('b'))

print("   Get non-existing key with default:", d.get('x', 'Not Found'))

# 5️⃣ update()
d.update({'d': 4})

print("5. After update:", d)

# 6️⃣ fromkeys()
new_dict = dict.fromkeys(['x', 'y', 'z'], 0)

print("6. Fromkeys:", new_dict)

# 7️⃣ pop()
removed_value = d.pop('b')

print("7. Pop key 'b':", removed_value)

print("   After pop:", d)

# 8️⃣ popitem()
last_item = d.popitem()

print("8. Popitem (last inserted):", last_item)

print("   After popitem:", d)

# 9️⃣ setdefault()
value = d.setdefault('e', 5)

print("9. Setdefault (add if missing):", value)

print("   After setdefault:", d)

# 🔟 copy()
copy_dict = d.copy()

print("10. Copy of dictionary:", copy_dict)

# 1️⃣1️⃣ clear()
d.clear()
print("11. After clear:", d)
