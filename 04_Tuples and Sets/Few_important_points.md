# In Python, you can perform set operations like union, intersection, and difference on sets using 
# both operators and methods. Sets are unordered collections of unique elements, which makes them 
# ideal for these mathematical operations.

* Sample sets
Let's use two example sets, A and B, to demonstrate these operations:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

1. Union
The union of two sets is a new set containing all the unique elements from both sets. 
Method: Use the union() method.
Operator: Use the pipe (|) operator. 

Example:
# Using the method
print(A.union(B))
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Using the operator
print(A | B)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

2. Intersection
The intersection of two sets is a new set containing only the elements that are common to both sets. 
Method: Use the intersection() method.
Operator: Use the ampersand (&) operator. 
Example:
# Using the method
print(A.intersection(B))
# Output: {4, 5}

# Using the operator
print(A & B)
# Output: {4, 5}

3. Difference
The difference between two sets is a new set containing the elements that are in the first set but not in the second. This operation is not commutative, meaning the order matters. 
Method: Use the difference() method.
Operator: Use the minus (-) operator. 
Example:

# Elements in A but not in B
print(A.difference(B))
# Output: {1, 2, 3}

# Elements in B but not in A
print(B.difference(A))
# Output: {8, 6, 7}

# Using the operator (elements in A but not in B)
print(A - B)
# Output: {1, 2, 3}

4. Symmetric difference
A related operation is the symmetric difference, which returns a set with all elements that are in either set, but not in both. 
Method: Use the symmetric_difference() method.
Operator: Use the caret (^) operator. 
Example:

print(A.symmetric_difference(B))
# Output: {1, 2, 3, 6, 7, 8}

print(A ^ B)
# Output: {1, 2, 3, 6, 7, 8}



