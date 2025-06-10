# Python Basics Exercises: Numbers and Math
# https://realpython.com/videos/numbers-and-math-exercises-overview/

# Creating Numbers

# Define Integer Literals
# Write a program that creates two variables, num1 and num2. Both num1 and num2 should be assigned the integer literal 25000000, one written with underscores and one without. Print num2 and num2 on two separate lines.

# num1 = 25_000_000
# num2 = 25000000
# print(num1)
# print(num2)

# Define Floating-Point Literals
# Write a program that assigns the floating-point literal 175000.0 to the variable num using E notation and then prints num in the interactive window.
# num = 175e3
# print(num)

# Find the Maximum Number
# Try to find the smallest exponent N for which 2e<N>, where <N> is replaced with your number, returns inf.
# print(2e308)

# ------------------------------------------

# Formatting Numbers

# Limit Decimal Places
# Print the result of the calculation 3 ** .125 as a fixed-point number with three decimal places.
# print(3 ** .125)
# print(f"{3 ** 0.125:.3f}")

# Format Currency
# Print the number 150000 as currency with the thousands grouped with commas. Currency should be displayed with two decimal places.
# print(f"${150000:,.2f}")

# Show a Percentage
# Print the result of 2 / 10 as a percentage with no decimal places. The output should look like 20%.
# print(f"{2 / 10:.0%}")

# ------------------------------------------

# Getting Numbers From the User

# Calculate the Exponent
# Write a program called exponent.py that receives two numbers from the user and displays the first number raised to the power of the second number.
# base = float(input("Input the first number (1.2) "))
# exponent = float(input("Input the second number (3) "))
# result = base ** exponent
# print(f"{base} to the power of {exponent} is {result}.")

# ------------------------------------------

# Using Math Functions

# Round Numbers
# Write a program that asks the user to input a number and then displays that number rounded to two decimal places. When run, your program should look like this:
# Enter a number: 5.432
# 5.432 rounded to 2 decimal places is 5.43.

# number = float(input("Enter a number "))
# print(f"{number} rounded 2 decimal places is {round(number, 2)}.")

# Calculate the Absolute Value
# Write a program that asks the user to input a number and then displays the absolute value of that number. When run, your program should look like this:
# Enter a number: -10
# The absolute number of -10 is 10.0.

# number = float(input("Enter a number (-10) "))
# print(f"The absolute value of {number} is {abs(number)}.")

# Check the Numeric Type

# Part 1: Write a program that asks the user to input two numbers by using input() twice, then displays whether the difference between those two numbers is an integer.

# Part 2: When run, your program should look like this:
# Enter a number: 1.5
# Enter another number: .5
# The difference between 1.5 and .5 is an integer? True!

# Part 3: If the user inputs two numbers whose difference is not integral, then the output should look like this:
# Enter a number: 1.5
# Enter another number: 1.0
# The difference between 1.5 and 1.0 is an integer? False!

# number1 = float(input("Enter a number: "))
# number2 = float(input("Enter another number: "))
# number_difference = number1 - number2
# print(f"The difference between {number1} and {number2} is an integer? {number_difference.is_integer()}!")