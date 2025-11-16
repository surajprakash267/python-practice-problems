"""
PROGRAM: Return Multiple Values
DESCRIPTION:
    This program demonstrates returning more than one value from a function.
    Values returned as a tuple.

LOGIC:
    - Input name, age, city
    - Return all three

EXAMPLE:
    Input: Suraj, 27, Delhi
    Output:
        Name: Suraj
        Age: 27
        City: Delhi
"""

def get_user_info():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")
    return name, age, city


if __name__ == "__main__":
    name, age, city = get_user_info()
    print(f"Name: {name}, Age: {age}, City: {city}")
