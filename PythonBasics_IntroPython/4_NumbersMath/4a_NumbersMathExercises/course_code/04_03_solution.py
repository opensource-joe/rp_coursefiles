"""
Using Math Functions - Check the Numeric Type

- Write a program that asks the user to input two numbers by using
 `input()` twice, then displays whether the difference between those
  two numbers is an integer.
- When run, your program should look like this:
    Enter a number: 1.5
    Enter another number: .5
    The difference between 1.5 and .5 is an integer? True!
- If the user inputs two numbers whose difference is not integral,
  then the output should look like this:
    Enter a number: 1.5
    Enter another number: 1.0
    The difference between 1.5 and 1.0 is an integer? False!
"""

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
diff = num1 - num2
print(
    f"The difference between {num1} and {num2} is an integer? "
    f"{diff.is_integer()}!"
)
