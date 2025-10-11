# Swap two numbers without a temporary variable

x = 23
f = 45
x, f = f, x # That’s the clean Pythonic way (tuple unpacking).
print(x, f)




# Alternate logic
x = 23
f = 45
x = x + f; f = x - f; x = x - f
print(x, f)

