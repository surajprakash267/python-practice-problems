# C. Check if a string is palindrome
# --------------------------------------------------


x = input("\n Enter the string to check palindrome: ")
y = x[::-1]
if x == y:
    print("Palindrome string")
else:
    print("Not a palindrome string")
