"""
Using Math Functions - Round Numbers

- Write a program that asks the user to input a number and then displays
  that number rounded to two decimal places.
- When run, your program should look like this:
    Enter a number: 5.432
    5.432 rounded to 2 decimal places is 5.43
"""

num = float(input("Enter a number: "))
print(f"{num} rounded to 2 decimal places is {round(num, 2)}")
