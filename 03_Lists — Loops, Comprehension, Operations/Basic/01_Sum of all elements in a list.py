#                           ✅ 1. Sum of All Elements in a List

#                               M1: Using built-in sum()

l = [2, 4, 5]
k = sum(l)
print(k)   # 11



#                                       M2: Using a loop


l1 = [2, 4, 6, 8, 0]
s = 0
for i in l1:
    s += i
print(f"The sum of the elements of the list is {s}") # The sum of the elements of the list is 20
