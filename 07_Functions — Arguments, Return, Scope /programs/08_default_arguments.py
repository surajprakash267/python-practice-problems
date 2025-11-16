"""
PROGRAM: Default Argument Values
DESCRIPTION:
    Demonstrates assigning default values to function parameters.

LOGIC:
    - If greeting not provided → "Hello" used

EXAMPLE:
    greet_user("World") → Hello, World!
    greet_user("Suraj", "Good Evening") → Good Evening, Suraj!
"""

def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"


if __name__ == "__main__":
    print(greet_user("World"))
    print(greet_user("Suraj", "Good Evening"))
