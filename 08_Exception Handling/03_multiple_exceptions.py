"""
Handling Multiple Exceptions - ValueError & TypeError
"""

try:
    value = int(input("Enter an integer: "))
except (ValueError, TypeError):
    print("Invalid input! Please enter a valid integer.")
except Exception as e:
    print("Some other exception occurred:", e)
