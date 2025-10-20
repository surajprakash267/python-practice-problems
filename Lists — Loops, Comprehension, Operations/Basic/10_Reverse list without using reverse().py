#M1:                Using slicing

l1 = [2, 5, 7, 5, 9, 87, 54, 900, 0, 20]
rev = l1[::-1]
print("Reversed list:", rev)


#M2:                    Using loop


l1 = [2, 5, 7, 5, 9, 87, 54, 900, 0, 20]
rev = []
for i in range(len(l1)-1, -1, -1):
    rev.append(l1[i])
print("Reversed list:", rev)


#M3:                        Using reversed()

l1 = [2, 5, 7, 5, 9, 87, 54, 900, 0, 20]
rev = list(reversed(l1))
print("Reversed list:", rev)
