"""
Custom Exception Example - Raise Error if age < 18
"""

class AgeTooSmallError(Exception):
    """Custom exception raised when age is below 18."""
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeTooSmallError("Age must be 18 or above.")
except AgeTooSmallError as e:
    print("Custom Error:", e)
except ValueError:
    print("Invalid input! Age must be a number.")
except Exception as e:
    print("Some unexpected exception occurred:", e)
