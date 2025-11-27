"""
Try/Except with Finally - code inside finally always executes
"""

try:
    a = 12
    b = 0
    c = a / b
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Done executing the block.")
