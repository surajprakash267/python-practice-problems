Python provides several built-in data structures for organizing and storing collections of data. Tuples, sets, and dictionaries are three of these fundamental types, each with distinct characteristics:

1. Tuples:
Ordered and Immutable: Tuples maintain the order of elements as they are added, and their contents cannot be changed after creation (elements cannot be added, removed, or modified).
Allow Duplicates: Tuples can contain multiple elements with the same value.
Indexed: Elements in a tuple can be accessed using numerical indices, similar to lists.
Syntax: Defined using parentheses ().

my_tuple = ("apple", "banana", "cherry", "apple")
print(my_tuple[0]) # Output: apple

2. Sets:
Unordered and Mutable: Sets do not maintain any specific order of elements, and elements can be added or removed after creation.
No Duplicates: Sets only store unique elements; any attempt to add a duplicate will be ignored.
Unindexed: Elements in a set cannot be accessed by index.
Syntax: Defined using curly braces {}.

my_set = {"apple", "banana", "cherry", "apple"}
print(my_set) # Output might be {'cherry', 'apple', 'banana'} (order is not guaranteed)
my_set.add("orange")
print(my_set)

3. Dictionaries:
Ordered and Mutable: Dictionaries, as of Python 3.7+, maintain the insertion order of key-value pairs. They are also mutable, allowing additions, removals, and modifications of entries.
Key-Value Pairs: Dictionaries store data as key-value pairs, where each unique key maps to a specific value.
No Duplicate Keys: Keys within a dictionary must be unique. Values can be duplicated.
Indexed by Keys: Values are accessed using their corresponding keys.
Syntax: Defined using curly braces {} with key-value pairs separated by colons :

my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(my_dict["model"]) # Output: Mustang
my_dict["color"] = "red"
print(my_dict)

* * * When to use each :
# The choice of which data structure to use depends on your specific needs. 

* Use a tuple: When you have a collection of items that should not change throughout the program's execution.
* Use a set: When you need a collection of unique items and order is not important. Sets are highly efficient for checking for the presence of an element.
* Use a dictionary: When you need to associate values with unique keys for efficient lookup and retrieval.