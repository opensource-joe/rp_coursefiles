# Python Basics: Scopes
https://realpython.com/courses/python-basics-scopes/

## Understanding Scope

Python scopes are implemented as dictionaries that map names to objects. You can look up objects and see their values. These dictionaries are commonly called namespaces. 

Check the global namespace dictionary with the help of globals() namespace function.

When we are talking about Python scope, we are talking about a concept. The namespace dictionary is the implementation of this concept. It's the implementation of scope. Scope and namespace are often used interchangeably and usually this is totally fine.

## Introducing the LEGB Rule

Whenever you use a name such as a variable or function name, Python searches through different scope levels to determine whether the name exists or not. To resolve the name, Python uses a specific order of scope levels. This order of looking up name is called, LEGB rule. 

LEGB:
- Local scope
- Enclosing scope
- Global scope
- Built-in scope

## Exploring the Local, Enclosing, and Global Scope

Local scope:
- Contains the names that you define inside a function.
- Every time you call a function, you're also creating a new local scope.

Enclosing scope:
- Special scope that only exists for nested functions.

Global scope:
- Top-most scope in a Python program, script, or module.
- Names are visible from everywhere in your Python code.
- There's only one global Python scope per program execution.
- Doesn't have to be on line one, shouldn't be wrapped in a function.

## Inspecting the Built-in Scope

Built-In scope:
- Automatically loaded by Python when you run a program or script.
- Contains names that are built into Python - keywords, functions, exceptions, and other attributes.
- Implemented as a standard library module named builtins.

## Using the global Statement

Global statement for brining global variable into a function.

```python
counter = 0

def update_counter():
    global counter # need this statement the pull in global variable
    counter = counter + 1

update_counter()
```

## Preventing Pitfalls

Good Programming Practices:
- Use local names rather than global names.
- Write self-contained functions.
- Use unique object names, no matter what scope you're in.
- Avoid global name modifications throughout your programs.