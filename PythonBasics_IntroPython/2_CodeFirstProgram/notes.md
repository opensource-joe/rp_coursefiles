# Python Basics: Code Your First Python Program
https://realpython.com/courses/python-basics-first-program/

Executing Python interactively works as a loop with three steps:
1. Python reads the code entered at the prompt.
2. Python evaluates the code.
3. Python prints the result and waits for more input.

This is commonly referred to as a read-evaluate-print loop (REPL) in Python. Python programmers often refer to this Python shell.

Syntax errors - a syntax error occurs when you write code that isn't allowed in the Python language.

Runtime errors - in the interactive window inside IDLE it catch syntax errors before a program starts running. In contrast, runtime errors only occur when the program is running. 

Traceback - when an error occurs, Python stops executing the program and displays several lines of text called a traceback. The traceback shows useful information about the error. Tracebacks are best read from the bottom up.

Creating Variables
In Python, Variables are names that can be assigned a value and then used to refer to that throughout your code.

Variables are fundamental to programming for two reasons:
1. Variables keep values accessible.
2. Variables give you context.

The assignment operator is a symbol, such as +, that performs an operation on one or more values. Values are assigned to variable names using a special symbol called the assignment operator =. The = operator takes the value to the right of the operator and assigns it to the name on the left.

Rules for valid Variable names:
- May contain uppercase and lowercase letters (A-Z, a-z).
- Digits (0-9).
- Underscores (_).
- Cannot begin with a digit.
- May contain Unicode characters.
    - Unicode is a standard for digitally representing characters used in most of the world's writing systems.

Variable case:
- mixedCase (numStudents).
- lower_case_with_underscores - snake case. Python norm. 

PEP 8 - Widely regarded as the official style guide for writing Python:
- [Python Style Guide - PEP8](https://pep8.org/)
- Follow standards in PEP 8 to ensure that your Python code is readable by most Python programmers.
- PEP stands for Python Enhancement Tool.
- A PEP is a design document used by the Python community to propose new features or changes to the language.

Inspecting Variables:
1. Type the name of the variable by itself at the prompt.
2. Use print([variable_name]).
3. Use type([variable_name]).

Comments:
1. Block comments start on a new line with #.
2. Inline comment begins on same line with #.

PEP 8 Comment Recommendations:
1. Comments should always be written in complete sentences.
2. Have a single space between the # and the first word of the comment.
3. Inline comments should start with two spaces after the code.
4. Comments that describe what is already obvious are unnecessary.
5. Comments should be used to clarify code. Why something was done a certain way.