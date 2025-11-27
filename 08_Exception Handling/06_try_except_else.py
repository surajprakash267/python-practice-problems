"""
Using Else Block with Try/Except
'else' executes only when no exception occurs
"""

try:
    f = open("example.txt", "r")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)
else:
    print("File opened successfully.")
    f.close()
