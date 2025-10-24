Method	Description	Example
.items()	Returns a view object with key–value pairs as tuples.	d.items() → dict_items([('a',1), ('b',2)])
.fromkeys()	Creates a new dictionary from given keys and a common value.	dict.fromkeys(['a','b','c'], 0) → {'a':0,'b':0,'c':0}
.values()	Returns a view object with all values.	d.values() → dict_values([1,2])
.keys()	Returns a view object with all keys.	d.keys() → dict_keys(['a','b'])
.update()	Updates dictionary with another dictionary or key-value pairs.	d.update({'c':3})
.get()	Returns value of a key safely (no error if key missing).	d.get('a', 'not found')
.pop()	Removes and returns value of a given key.	d.pop('a')
.popitem()	Removes and returns last inserted (key, value) pair.	d.popitem()
.clear()	Removes all items from the dictionary.	d.clear() → {}