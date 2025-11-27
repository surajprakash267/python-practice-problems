Exception handling in Python allows your program to respond to errors gracefully instead of crashing.
This README explains all concepts with examples and shows how to fix real problems using try/except/else/finally and custom exceptions.
🔥 1. What Is an Exception?
An exception is an event that occurs during program execution that disrupts the normal flow.
Example errors:
Error	Meaning
ZeroDivisionError	Dividing a number by zero
ValueError	Input conversion failed
FileNotFoundError	File does not exist
TypeError	Wrong data type used
KeyError	Accessing missing dictionary key
Without handling exceptions, Python stops the program immediately.
🛡 2. Why Exception Handling Is Needed?
✔ Prevent program crashes
✔ Handle unexpected user input
✔ Continue execution after an error
✔ Build stable automation scripts
✔ Improve debugging
✔ Control error flow for clean output
Example (unhandled error):
a = 10 / 0
print("End")
❌ Program crashes
❌ "End" never prints
🧩 3. try / except – Basic Error Handling
✔ Structure:
try:
    # code that may raise an error
except SomeError:
    # solution for that error
Example:
try:
    c = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
🧠 Problem Solved:
Prevents the program from crashing
Shows a clear message
🔥 4. Handling Multiple Exceptions
Sometimes more than one error can occur.
Structure:
try:
    # risky code
except (Error1, Error2):
    # handle both
Example:
try:
    num = int(input("Enter a number: "))
except (TypeError, ValueError):
    print("Please enter a valid integer.")
🧠 Problem Solved:
Avoids crashes from incorrect input types
Accepts only valid values
🟦 5. Catching All Exceptions (Not Recommended Always)
except Exception as e:
    print("Unexpected error:", e)
Use this only when:
✔ You want to log unknown issues
✔ You're writing production-level automation scripts
✔ You need to handle any possible error without crash
🟢 6. try / except / else
else runs only when no exception occurs.
Example:
try:
    f = open("example.txt", "r")
except FileNotFoundError:
    print("File not found.")
else:
    print("File opened successfully.")
    f.close()
🧠 Problem Solved:
Clean separation between error handling and successful execution
🟡 7. try / except / finally
finally always runs — whether error occurs or not.
Example:
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Cleanup done.")
🧠 Problem Solved:
Closing file handles
Releasing resources
Cleanup tasks
🔴 8. Custom Exceptions
When built-in exceptions are not enough, you create your own.
Structure:
class CustomError(Exception):
    pass
Example:
class AgeTooSmallError(Exception):
    """Raised when age < 18."""
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeTooSmallError("You must be 18+ to register.")
except AgeTooSmallError as e:
    print("Custom Error:", e)
🧠 Problem Solved:
Gives clear, domain-specific error messages
Used in API testing, validations, business logic, frameworks
📂 9. Safe File Handling With Exceptions
Proper file handling prevents runtime crashes.
Example:
try:
    with open("example.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")
🧠 Problem Solved:
Prevents crash if file missing
Automatically closes file
Prevents memory leaks
⚙️ 10. Common Real Problems & How to Solve Them
🔹 Problem 1: Program crashes due to invalid input
Solution: Use ValueError handling.
try:
    x = int(input("Enter number: "))
except ValueError:
    print("Please enter digits only.")
🔹 Problem 2: Division by zero
Solution: Handle ZeroDivisionError.
try:
    result = a / b
except ZeroDivisionError:
    print("Denominator cannot be zero.")
🔹 Problem 3: File missing
Solution: Handle FileNotFoundError.
try:
    open("abc.txt")
except FileNotFoundError:
    print("File doesn't exist.")
🔹 Problem 4: Need custom validation
Solution: Create a custom exception.
class InvalidScore(Exception):
    pass
🔹 Problem 5: Always close resources
Solution: Use finally.
try:
    f = open("test.txt", "r")
finally:
    f.close()
🧠 11. When to Use Which Block?
Situation	Use
Risky code	try
Known error	except
Run if no error	else
Run always	finally
Domain-specific validations	Custom exception
Multiple possible errors	multiple except blocks
🏁 12. Summary
✔ Exceptions stop program flow
✔ Use try/except to prevent crashes
✔ Use else when success logic is needed
✔ Use finally for cleanup
✔ Create custom exceptions for business logic
✔ Exception handling makes code robust and readable