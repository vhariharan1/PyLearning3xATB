# Task #2
#
# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8

num = 2
sq = num ** 2
c = num ** 3
print("Square of", num, "is", sq)
print("Cube of", num, "is", c)

# Create a program that takes two numbers as input
# and prints whether the first number is greater than, less than, or equal to the second number.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)