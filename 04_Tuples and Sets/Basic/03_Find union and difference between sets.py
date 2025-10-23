#✅ 3️⃣ Union and Difference
# The union of two sets contains all unique elements from both sets.

l1 = {2,5,7,5,9,87,54,900,0,20}
l2 = {4,2,9,20}

# Using the union() method
print(l1.union(l2))   # Union
print(l1 | l2)        # Union (alternative)



#The difference of two sets (e.g.set1 - set2) contains elements that are in the first set but not in the second set.
# Using the difference() method
print(l1.difference(l2))  # Difference
print(l1 - l2)            # Difference (alternative)


#🟢 Extra Tip: You can also find symmetric difference (elements not common in both):

print(l1 ^ l2)  # or l1.symmetric_difference(l2)

