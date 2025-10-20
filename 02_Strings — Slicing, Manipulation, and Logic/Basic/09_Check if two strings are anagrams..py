 #          Check if two strings are anagrams.

 # 👉 Two strings are anagrams if they contain the same characters with same frequency, in any order.

#                       ✅ Method 1 (using sorted())

s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

"""
Answer: 
Enter first string: listen
Enter second string: silent
The strings are anagrams.
"""


#                 ✅ Method 2 (using dictionary count)

from collections import Counter

s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

if Counter(s1) == Counter(s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
