"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

Addition = float(num1 + num2)
Subtraction = float(num1 - num2)
Multiplication = float(num1 * num2)
Division = float(num1/num2)
print("The addition of the given numbers is:", Addition)
print("The subtraction of the given numbers is:", Subtraction)
print("The multiplication of the given numbers is:", Multiplication)
print("The division of the given numbers is:", Division)

