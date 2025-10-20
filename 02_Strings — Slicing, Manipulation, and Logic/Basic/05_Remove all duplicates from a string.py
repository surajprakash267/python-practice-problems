#.                      Remove all duplicates from a string.


# Method 1:  Keep order of first occurrences

s = "programming"
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result) #    progamin

#  Method 2:  If order doesn’t matter

s = "programming"
print("".join(set(s)))

#Note: ⚠️ But remember: set() does not preserve order.

