"""
PROGRAM: Palindrome Checker
DESCRIPTION:
    This program checks whether a given string or number is a palindrome.
    A palindrome reads the same forward and backward.

LOGIC:
    1. Convert input to lowercase.
    2. Remove spaces.
    3. Compare the string with its reverse.

EXAMPLE:
    Input:  "madam"
    Output: Palindrome

"""

def is_palindrome(n):
    s = str(n).replace(" ", "").lower()
    return s == s[::-1]


if __name__ == "__main__":
    s = input("Enter a number/string: ")
    if is_palindrome(s):
        print(f"{s} is a Palindrome.")
    else:
        print(f"{s} is NOT a Palindrome.")
