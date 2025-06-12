# Python Basics Exercises: Functions and Loops
# https://realpython.com/courses/python-exercises-functions-loops/

# Review Exercises

# Greet Someone
# Write a function called greet() that takes one string parameter called <name> and displays the text "Hello, <name>!", where <name> is replaced by the value of the <name> parameter.

# def greet(name):
#     print(f"Hello, {name}!")

# greet("Joe")

# Cube
# Write a function called cube() that takes one number parameter and returns the value of that number raised to the third power. Test the function by calling your cube() function on a few different numbers and displaying the results.

# def cube(number):
#     return number ** 3 #can also use pow(number, 3)

# print(cube(3))

# -------------------------------------------------

# Temperature Conversion Challenge

# Convert Celsius to Fahrenheit
# 1. convert_cel_to_far(), which takes one float parameter representing degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit using the following formula: F = C * 9/5 + 32.
# 2. Prompt the user to enter a temperature in degrees Celsius and then display the temperature converted to Fahrenheit.
# 3. Display all converted temperatures rounded to two decimal places.

# Convert Fahrenheit to Celsius
# 1. convert_far_to_cel(), which takes one float parameter representing degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius using the following formula: C = (F - 32) * 5/9.
# 2. Prompt the user to enter a temperature in degrees Fahrenheit and then display the temperature converted to Celsius.
# 3. Display all converted temperatures rounded to two decimal places.

# def convert_cel_to_far():
#     celsius_temp = float(input(f"Please enter a temperature in Celsius: "))
#     return round(celsius_temp * 9 / 5 + 32, 2)

# print(convert_cel_to_far())

# def convert_far_to_cell():
#     far_temp = float(input(f"Please enter a temperature in Fahrenheit: "))
#     return round((far_temp - 32) * 5 / 9)

# print(convert_far_to_cell())

# -------------------------------------------------

# More Review Exercises

# Print Integers
# Write a For loop that prints out the integers 2 through 10, each one a new line using range().

# for n in range(2, 11):
#     print(n)

# Display the Doubles
# Write a function called doubles() that takes a number as its input and doubles it. Then use doubles() in a loop to double the number 2 three times, displaying each result on a separate line.

# def doubles(num):
#     return num * 2

# my_num = 2
# for _ in range(3): # Use underscore for throwaway variable
#     my_num = doubles(my_num)
#     print(my_num)
    
# -------------------------------------------------

# Investment Challenge
# Write a program that tracks the growing amount of an investment over time. The initial deposit for an investment is called the principal amount. Each year, the amount increases by a fixed percentage, called the annual rate of return.

# 1. Function invest() with three parameters: principal amount, annual rate of return, and number of years to calculate. def invest(amount, rate, years):

# 2. Print out the amount of the investment rounded to two decimal places at the end of each year for the specified number of years.

# Example: calling invest(100, .05, 4) should result in:
# year 1: $105.00
# year 2: $110.25
# year 3: $115.76
# year 4: $121.55

# 3. Prompt user to enter amounts and call the function to display values entered by the user.

def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:.2f}")

amount = float(input("Please enter the amount (100): "))
rate = float(input("Please enter the rate (.05): "))
years = int(input("Please enter the number of years (4): "))

invest(amount, rate, years)