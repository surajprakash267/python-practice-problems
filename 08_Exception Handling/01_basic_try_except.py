"""
Basic try/except example - Handling ZeroDivisionError
"""

try:
    a = 12
    b = 0
    c = a / b
except ZeroDivisionError:
    print("Cannot divide a number by zero.")
