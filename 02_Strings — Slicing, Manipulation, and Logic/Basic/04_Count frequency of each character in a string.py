#               Count frequency of each character in a string.


# Method 1: Using dictionary:

s = "hello world"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)   # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


#                    Method 2:  Shortcut (using collections.Counter)

from collections import Counter

s = "hello world"
print(Counter(s))  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
