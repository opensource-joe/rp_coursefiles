# Python Data Types and Operations

## Strings and String Methods

### String Data Type
- Strings are one of the fundamental Python data types.
    - Data Types: What kind of data a value represents.
        - Strings are used to represent text.
    Other types:
        - Numeric types: int (integers), float (floating point numbers).
        - Booleans (True, False).
        - Sequence types - list, tuple, string.

- Strings are a fundamental data type.
    - Can't be broken into smaller values of a different type.
    - Unlike a compound data type, which are known as data structures.

- Strings have three important properties:
1. Contain individual letters or symbols called characters.
2. Have a length, defined as the number of characters contained.
3. Characters in a string appear in a sequence, each character has a numbered position called an index.

Quotes around the str are known as deliminators. Needs to single or multiple quotation marks. To include a quotation mark inside a str, use a "\" to escape.

Length of a str is determined by len([string]).

Multiline strings:
- PEP 8 recommends each line of Python code contain no more than 79 characters - including spaces.
- Two techniques to break a string across multiple lines.
    1. Add a backslash (\) at the end of all but the last line.
    2. Use triple quotes as delimiters (""" or ''').

### Concatenating, Indexing, and Slicing
Concatenation - joins two strings together.
- Concatenate with a "+" symbol. ```string1 + string2```

Indexing - gets a single character from a string.
- Each character in a string has a numbered position called an index.
- Individual characters can be accessed by using the index.
- Place the index inside a pair of square brackets after the string. ```my_string[0]```
- Index count starts with zero.
- Negative indexing in working backwards from end of string with -1.
- Grab last character in string. ```final_index = len([variable]) -1```

Slicing - gets several characters from a string at once.
- Extract a portion of a string, called a substring.
- Insert a colon between two index numbers. ```[0:5]```

- For slicing, indices, behave more like boundaries around characters.
- Negative slicing works by the same rules. A slice of [x:y] starts from the character at index x, and goes up to, but does not include the character at the index y.

- Omitting the index before the colon, starts with the first character. [:5]
- Omitting the index after the colon, ends with the last character. [5:]
- Omitting both indexes returns the whole string.

Strings are immutable - cannot change once they are created. To alter a string, you must create a new one through assignment.

### Manipulating Strings with String Methods
- Built in methods are known as dot methods.

- .lower() - converts all chr in str to lowercase letters.
- .upper() - converts all chr in str to upper case.

- .rstrip() - removes trailing spaces from right side of string.
- .lstrip() - removes trailing spaces from left side of string.
- .strip() - removes whitespaces from both left and right sides.

- .startswith() - determine if a string starts with a particular string.
- .endswith() - determine if a string ends with a particular string.

### Interacting with User Input
Using input() to interact with the user.

### Working with Strings and Numbers
Using Strings with Arithmetic Operators:
- The + operator concatenates two strings together.
- The * operator concatenates multiple copies of a string.

Converting Strings to Numbers:
- int() - converts objects into whole numbers.
- float() - converts objects into numbers with decimal points.

Converting Numbers to Strings:
- str() - returns a string version of an object.

### Streamlining Your Print
Formatted string literals commonly known as f-strings.
- A string literal with the letter f before the opening quotation mark.
- Variable names surrounded by curly braces {} are replaced by their corresponding values without using str().

```python
day = "Tuesday"
eggs = 2
bacon = 3

f"{day}'s breakfast is {eggs} eggs and {bacon} pieces of bacon."
```

### Finding a String in a String
- .find() - finds the location of one string within another string (a substring). .find(<sub>) returns the index of the first occurrence of the string passed to it.
- .replace() - replaces each instance of a substring with another string. .replace(<old>, <new>)

---

## Numbers and Math