# Task #1

# Explain the difference between the = operator and the == operator in Python.

# '=' is used to assign value to a variable. It is called assignment operator.
# For example, name = "Hari", here value "Hari" is assigned to the variable 'name'
# '==' is used to check equality
i = 2
if i == 2:
    print("i is equal to 2")
else:
    print("i is not equal to 2")

# What does the ** operator do in Python, and how is it used?
# ** operator is used to denote power of a number
a = 2
print(a ** 2)

# What does the ^ operator do in Python, and in what context is it commonly used?
# '^' is an XOR operator, it can be used to swap two numbers
b = 4 # binary = 0100
c = 5 # binary = 0101
print(b ^ c) # binary = 0001 = 1

d = 6 # binary = 0110
e = 3 # binary = 0011
print(d ^ e) # binary = 0101 = 5