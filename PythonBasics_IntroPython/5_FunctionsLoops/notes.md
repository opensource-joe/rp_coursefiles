# Python Basics: Functions and Loops
https://realpython.com/courses/python-basics-functions-loops/

## Overview

Functions are the building blocks of almost every Python program. Functions break code into smaller chunks. They are great for defining actions that a program will execute several times. 

Loops for repeating code, perform a task over and over again. 

## Executing a Function

Built-in Functions:
- type() - check the type of a variable.
- len()  - length of a variable.

Two parentheses to call a function.

Executing a Function:
1. Call: Any arguments are passed to the function as input.
2. Execution: Some action is performed with the arguments.
3. Return: The original function call is replaced with the return value.

All Functions return a value even if it is NoneType.

## Creating Your Own Functions

Naming a Function:
1. Letters
2. Numbers
3. Underscores
* A function must not start with a number.

Parentheses are not part of the functions name. Python does support leading underscores to indicate that a function is private to the current module or class.

User defined functions need the Def keyword. Parameter has no value, placeholder for a future value.

```python
def shout_and_return(input_string):
    loud_input = input_string.upper()
    print(loud_input)
    return loud_input

shout_and_return("test")
```

## Documenting Your Functions

When you create own functions, should always document them. This should be done with a docstring at the top of the function body. Docstring defines the function and parameters.

```python
def shout_and_return(input_string):
    """Print and return a string in uppercase."""
    loud_input = input_string.upper()
    print(loud_input)
    return loud_input

shout_and_return("test")
```

## Writing While and For Loops

Loop is a block of code that repeats a specific number of times or until a some condition is met. Python has two types of loops, While and For loops.

For loop to repeat code until a condition is met.

```python
n = 1
while n < 5:
    print(n)
    n = n + 1 #increments n by 1 until it reaches 5, keeps from infinite loop
```

```python
num = float(input("Enter a positive number: "))

while num <= 0:
    print("That's not a positive number!")
    num = float(input("Enter a positive number: "))
```

For loop to repeat code a specific number of times.

```python
for letter in "Donut":
    print(letter)
```

Using range() with For and While loops.

For loop:
```python
for n in range(1, 5):
    print(n)
```

While loop:
```python
n = 1

while n < 5:
    print(n)
    n = n + 1
```

Can nest loops inside of loops. Can go more than two levels deep.

```python
for n in range(1, 4):
    for j in range(1, 4):
        print(f"n = {n} and j = {j}")
```