# Count digits, letters, and spaces in a string

"""
Logic:
Go through each character and check what type it is.

🧠 Tip:
Use .isalpha(), .isdigit(), .isspace() — very handy string functions!

"""

text = input("Enter a string: ")

letters = digits = spaces = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1

print(f"Letters: {letters}, Digits: {digits}, Spaces: {spaces}")
