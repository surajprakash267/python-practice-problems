This file explains all important concepts with examples.

# Python Concepts – Quick Definitions

A reference guide for important function-related concepts.

---

## 🔹 Lambda Function
Small anonymous function defined using:
```python
lambda arguments: expression

Example:
square = lambda x: x*x

🔹 map()
Applies a function to each item of an iterable.
map(function, iterable)

Example:
map(lambda x: x*2, [1,2,3])

🔹 filter()
Filters items based on condition.
filter(function, iterable)

Example:
filter(lambda x: x%2==0, [1,2,3,4])

🔹 reduce()
Reduces elements into a single value.
from functools import reduce
reduce(lambda a,b: a+b, [1,2,3])

🔹 *args
Allows passing variable number of positional arguments.
def f(*args):
    print(args)
    
🔹 **kwargs
Variable number of keyword arguments.
def f(**kwargs):
    print(kwargs)
    
🔹 Recursion
Function calling itself.
def fact(n):
    return 1 if n == 0 else n * fact(n-1)
    
🔹 Closure
Inner function remembers variables from outer function.
def outer(msg):
    def inner():
        print(msg)
    return inner
    
🔹 Default Arguments
Specified default values for parameters.
def greet(name, msg="Hello"):
    return msg + name
    
    
📌 Purpose
Use this file to revise anytime you forget a concept.
