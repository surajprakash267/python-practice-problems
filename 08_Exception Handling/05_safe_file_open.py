"""
Safe File Handling - using try/except with file operations
"""

try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'example.txt' does not exist.")
except Exception as e:
    print("Some exception occurred:", e)
