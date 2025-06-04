# String Data Type

# 1. Print a string that uses double quotation marks inside the string.
# print("This is a string!")

# 2. Print a string that uses an apostrophe inside the string.
# print("This isn't messing up with the apostrophe.")

# 3. Print a string that spans multiple lines with whitespace preserved.
# print("This is a message \
#             with whitespace \
#       and multiple lines.")

# 4. Print a string that is coded on multiple lines but gets printed on a single line.
# print('Text on multiple '
#       'lines with no '
#       'spaces.')

# -------------------------------------------------

# Concatenating, Indexing, and Slicing

# 1. Create a string and print its length using len().
# example_string = "This is a string!"
# print(len(example_string))

# 2. Create two strings, concatenate them, and print the resulting string.
# string1 = "The cow flew over "
# string2 = "the moon."
# print(string1 + string2)

# 3. Create two strings, use concatenation to add a space between them, and print the result.
# string1 = "The cow flew over"
# string2 = "the moon."
# print(string1 + " " + string2)

# 4. Print the string "zing" by using slice notation to specify the correct range of characters in the string "bazinga".
# characters = "bazinga"
# print(characters[2:6])

# -------------------------------------------------

# 1. Write a program that converts the following strings to lowercase. "Animals", "Badger", "Honey Bee", "Honey Badger". Print each lower-case string on a separate line.
# words = "Animals", "Badger", "Honey Bee", "Honey Badger"
# for word in words:
#     print(word.lower())

# 2. Repeat exercise 1, but convert each string to uppercase instead of lowercase.
# words = "Animals", "Badger", "Honey Bee", "Honey Badger"
# for word in words:
#     print(word.upper())

# 3. Write a program that removes whitespace from the following strings, then print out the strings with the whitespace removed:
# string1 = "  Filet Mignon"
# string2 = "Brisket  "
# string3 = "  Cheeseburger  "

# print(f"{string1.lstrip()}, {string2.rstrip()}, and {string3.strip()}")

# 4. Write a program that prints out the result of .startswith("be") on each of the following strings.
# string1 = "Becomes"
# string2 = "becomes"
# string3 = "BEAR"
# string4 = " bEautiful"

# print(f"{string1.startswith("be")}, {string2.startswith("be")}, {string3.startswith("be")}, and {string4.startswith("be")}")

# 5. Using the same four strings from #4, write a program that uses string methods to alter each string so that .startswith("be") returns True for all of them.
# string1 = "Becomes"
# string2 = "becomes"
# string3 = "BEAR"
# string4 = " bEautiful"

# print(f"{string1.lower().startswith("be")}, {string2.startswith("be")}, {string3.lower().startswith("be")}, and {string4.lower().strip().startswith("be")}")

# -------------------------------------------------

# Interacting with User Input

# 1. Have a program display user input.
# name = input("Enter your name: ")
# print("Hello, " + name + "!")

# 2. Have a program display user input in lowercase.
# name = input("Enter your name: ")
# print("Hello, " + name.lower() + "!")

# 3. Have a program display the number of characters in the input.
# name = input("Enter your name: ")
# print(len(name))

# -------------------------------------------------
# TODO: Complete the exercises below
# Working with Strings and Numbers

# 1. Create a string containing an integer, then convert that string into an actual integer object using int(). Test the new object is a number by multiplying it by another number and displaying the result.

# 2. Repeat the previous exercise, but use a floating-point number and float().

# 3. Create a string object and an integer object, then display them side by side with a single print using str().

# 4. Write a program that uses input() twice to get two numbers from the user, multiplies the numbers together, and displays the result. Example: The product of 2 and 4 is 8.0.

# -------------------------------------------------

# Streamlining Your Print

# 1. Create a float object named weight with the value 0.2, and create a string object named animal with the value "newt". Use these objects to print the following string using only string concatenation: 0.2 kg is the weight of a newt.

# 2. Display the same string by using .format() and empty {} placeholders.

# 3. Display the same string by using f-strings.

# -------------------------------------------------

# Finding a String in a String

# 1. In one line of code, display the result of trying to .find() the sub-string "a" in the string "AAA". The result should be -1.

# 2. Replace every occurrence of the character "s" with "x" in the string "Somebody said something to Samantha".

# 3. Write a program that accepts user input with input() and displays the result of trying to .find() a particular letter in that input.

# Challenge: Turn Your User Into an L33t H4xOr
# 1. Write a program called translate.py that asks the user for some input with the following prompt: Enter some text:
# 2. Use .replace() to convert the text entered by the user into leetspeak by making the following changes to lowercase letters.

# The letter a becomes 4
# The letter b becomes 8
# The letter e becomes 3
# The letter l becomes 1
# The letter o becomes 0
# The letter s becomes 5
# The letter t becomes 7

# 3. The program should then display the resulting string as output. Enter some text: I like to eat eggs and spam. I 1ik3 70 347 3gg5 4nd 5pm4m.