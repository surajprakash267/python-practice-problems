#M1 : Using String Slicing

"""
Logic:
s[::-1] reverses the string.

"""
s = input("Enter a string or number: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#M2:   Using Recursion

"""
Logic:
Compare first and last chars, call recursively on inner part.

"""
def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

s = input("Enter string or number: ")
print("Palindrome" if is_palindrome(s) else "Not Palindrome")

#M3 :   One-liner using Lambda

is_palindrome = lambda s: s == s[::-1]
print(is_palindrome(input("Enter: ")))
