"""
PROGRAM: Closure Example
DESCRIPTION:
    Demonstrates closure where inner function uses outer function variables.

LOGIC:
    - outer() defines a variable
    - inner() uses the variable even after outer() ends
    - outer() returns inner()

EXAMPLE:
    fn = outer("Hello")
    fn()  → prints "Hello"
"""

def outer(msg):
    def inner():
        print("Message:", msg)
    return inner


if __name__ == "__main__":
    fn = outer("Hello Suraj!")
    fn()
