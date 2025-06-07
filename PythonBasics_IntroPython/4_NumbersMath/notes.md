# Python Basics: Numbers and Math
https://realpython.com/videos/python-basics-numbers-math-overview/

## Numeric Types in Python

Three numeric types built-in to Python:
1. Integers
2. Floating point numbers
3. Complex numbers

All numbers have a built-in sign and can store positive and negative numbers. No max or min value. Floats do.

Additional types:
1. Decimal
2. Fraction

## Integers

Whole number with no decimal places. No fractional part. Can be positive and negative. Use "_" for commas in large numbers. Can use binary system to represent numbers.

## Floating-Point Numbers

Second most commonly used number in Python. Numbers with decimal points.

Use the exponent: 4.2e7 or use format(-4.2E-7, ".8f"). Use float("inf") or float("-inf") to search for max or min values.

float(nan) for not a number.

Float has a fixed limit. Can use: import sys; sys.float_info.max.

## Arithmetic Operators and Expressions

Seven arithmetic operators and they are all binary meaning they take two arguments each. Both arguments of an operator are called their operands.
- Addition 5 + 2
- Subtraction 5 - 2
- Multiplication 5 * 2
- Exponentiation 5 ** 2
- Division 5 / 2 - result is always a float
- Floor division 5 // 2 - returns an int, rounds the remainder
- Modulus 5 % 2 - calculates remainder of division

Dividing by zero results in an error.

Operator precedence - follows arithmetic operations.

## Floating-Point Representation Error

Fixed vs. floating-point numbers. Floating-point notation allows the decimal to move around to present the fraction. Float-point number is an approximation. Use decimal notation for finance programs for better accuracy.

## Math Functions and Number Methods

round() - takes floating point number and rounds to closes integer. Challenge with .5, rounds to nearest even number. Can pass second argument for number of decimal places.

abs() - takes number and returns number without the sign. Always get positive value.

pow() - more explicit way to raise number to the power.

.is_integer() and .as_integer_ratio() for examining floats and integers. int.bit_length() and int.bit_count() as integer methods.

## Numbers Formatted as Strings

format() or f-strings - for displaying numbers in a string.

Use a format specifier to for decimal places {price:.2f}. Many [format string](https://docs.python.org/3/library/string.html#formatstrings) literals.

## Complex Numbers

Rarely used outside of scientific and computer graphics. Consist of real and imaginary parts.

z = 3 + 2j

.conjugate() - flips the sign of the number.