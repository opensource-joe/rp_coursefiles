# Python Basics: Lists and Tuples
https://realpython.com/courses/python-basics-lists-tuples/

## Python Tuples

### Think of Tuples as Rows

What is a tuple?
- A tuple is a finite, ordered, immutable sequence of values.
- Python borrows the name and the notation from mathematics.
	- Each element is seperated by a comma.
	- All elements are surrounded by a pair of parentheses.
	- E.g., (1, 2, 3)
	
 Think of a tuple as a read-only database record.
 - A finite sequence of values.
 - Has a fixed structure.
 - Has fixed values.
 - Contains a variety of data types (text, numbers, ...).
 - Contains related data.
 
***A read-only database record.***
 
### Create Tuples

Two ways: tuple literals and built-in tuple().

Tuple literal:
- Comma-separated values.
- Surrounded by parantheses.

	(1, 2, 3)
	(1, "Adisa", "Software Engineer")

Built-in tuple():
- tuple() can be used to create a tuple from another sequence type.

	typle("Python")
	("P", "y", "t", "h", "o", "n")

### Index Tuples and Strings

Similarities Between Tuples and Strings
- Tuples have a length.
- Tuples support indexing and slicing.
- Tuples are immutable.
- Tuples are iterable.

Tupples have a length:

	numbers = (1, 2, 3)
	len(numbers)

Each element in a tuple has a numbered position called an index.
- Access individual elements through the index.
- Place the index number inside a pair of square brackets after the tuple.

	numbers = (1, 2, 3)
	numbers[1]
	
### Slice Tuples and Strings

Slicing:
- To extract a portion of a tuple, insert the colon between two index numbers: [0:2].

	odd_numbers = (1, 3, 5, 7, 9)
	odd_numbers[2:4]

- The slice [x:y] starts from the element at index x.
- The slice goes up to, but does not include, the element at index y.

### Explore Immutability in Tuples and Strings

Tuples are immutable. You can't change the value of an element in a tuple after creation.

### Tuples and Strings are Iterable

Tuples are iterable, you can loop over them.

```python
numbers = (1, 2, 3)

for number in numbers:
    print(number)
```

```python
word = "Python"

for char in word:
    print(char)
```

### Tuple Unpacking

You can create a tuple by listing values separated by commas where the parantheses are optional.

	rbg_lime_green = 50, 205, 50

	type(rbg_lime_green)

You can assign elements of a tuple to multiple variables by unpacking it.

	red, green, blue = rgb_lime_green

With tuple unpacking, you can assign multiple variables in one line.

	employee_id, name, role = 1, "Adisa", "Software Engineer"

Don't overdo it, only assign multiple variables via tuple unpacking if it makes your code more readable.

For unpacking to work, the number of variables must match the number of values.

### Inspect Database Return Types

Tuple unpacking:
- Remember that tuples are like database records.
- Python libraries that allow you to fetch data from databases may return rows as tuples.
- You can unpack these if you need access to individual values.

### Check for the Existance of Elements

Check for the existance of values using the "in" keyword.

	vowels = ("a", "e", "i", "o", "u")
	"o" in vowels # returns True

	numbers = (1, 2, 3)
	1 in numbers # returns True

### Return Multiple Values From a Function

```python
def get_stats(sequence):
    return max(sequence), min(sequence)

numbers = (1, 2, 3)

get_stats(numbers) # returns (3, 1)

type(get_stats(numbers)) # returns <class 'tuple'>
```

Can use tuples to return multiple values of a function.

## Python Lists

### Think of Lists as Lists

What is a list?
- A list is an ordered, mutable sequence of values.
- Each element is separated by a comma.
- All elements are surrounded by a pair of square brackets.
- Example: [1, 2, 3]

Lists are similar to tuples Both:
- Can contain items of any data type.
- Are Indexed by integers starting at 0.
- Support slice notation.
- Support `in` to check for the existence of elements.
- Are iterable.

Lists are different from tuples because they are mutable. You can change elements in a list after you've created it.

```python
numbers = [1, 2, 3]
numbers[0] = "One"

numbers #returns ['One', 2, 3]
```

### Create Lists

- List literal: [1, 2, 3]
- Built-in list(): list(<sequence>)
- String method .split(): str.split(<separator>)
    - Can say where to split the string. Most common way is on a whitespace.

```python
"The quick brown fox".split() #will split the str on whitespaces.
```

### Work with Lists

Indexing:
`numbers = [1, 2, 3, 4]`
`numbers[1]`

Slicing:
`numbers[1:2]`

Membership testing:
`2 in numbers`
`"Bob" in numbers`

Iteration:
```python
numbers = [1, 2, 3, 4]

for number in numbers:
    if number % 2 == 0:
        print(number)
```

### Change Elements in a List

```python
numbers = [1, 2, 3]
numbers[1] = 20 #prints [1, 20, 3]

numbers[1:] = [200, 300, 400] #prints [1, 200, 300, 400]
```

### Adding and Removing Elements

- .insert(i, x): pass index where to insert element, then the element.
- .append(x): pass as argument and it adds to end of the list.
- .extend(<iterable>): pass an argument as an iterable and adds to end of list. Add more than one element.
- .pop(i): pass an index to remove an element from the list. Don't pass the index, it will take off the last element.

### Working with Lists of Numbers

You can perform mathematical operations on collections using built-in functions:
- sum(): adds all items in a collection.
- min()
- max()

### Create List Comprehensions

```python
numbers = (1, 2, 3)

squares = []
for number in numbers:
    squares.append(number**2)
```

Python has list comprehensions to do what last three lines of code completed. A list comprehension is shorthand for a for loop.

```python
squares = [num**2 for number in numbers]
```

### Nesting Lists

Nested collection is a list inside of a list. Can also nest tuples.

    maori_words = [
        ["whāna", "family],
        ["kai", "food"],
        ["aroha", "love"]
    ]

Access using double index notation.

    maori_words[2][0] #returns 'aroha'
    maori_words[2][1] #returns 'love'

You can nests lists as deeply as you want to but don't do it unless you have a good reason.

### Create a Second Reference to a List Object

Copying lists. Variable names are references to objects in memory.

```python
matrix = [[1, 2], [3, 4]]

the_matrix = matrix
the matrix[-1] = ["Neo", "Trinity"]

the_matrix #returns [[1, 2], ['Neo', 'Trinity']]
matrix #returns [[1, 2], ['Neo', 'Trinity']]

# Both variables point to the same object. Find an element object identifier with id(<element>).
```

### Create a Shallow Copy of a List

Shallow copies reference to objects but not that actual objects.

```python
the_matrix = matrix[:] # makes a shallow copy of the matrix list and assigns a new object ID.

id(matrix)
```

### Create a Deep Copy of a List

Only deep copy creates a truly independent copy of an object. Use import copy.

```python
import copy

matrix = [[1, 2], [3, 4]]
the_matrix = copy.deepcopy(matrix)
the_matrix[0][0] = "The Oracle"

the_matrix # produces updated list with "The Oracle"
maxrix # keeps original list objects
```
Only with deep copy can you truly make an independent copy of an object.

### Sort Lists

Use .sort() method.

```python
colors = ["red", "yellow", "green", "blue"]
colors.sort() # sorts the list in alphabetical order because it's strings. Can do same with numbers for ordering.
```
Lists with strings sort with unicode code points.

Can use .sort(reverse=True) to sort in reverse order.

### Pass Built-in Function for Sorting

Can pass key to a function for sorting.

```python
colors = ["red", "yellow", "green", "blue"]
colors.sort(key=len)
```
The .sort() method accepts a function as an argument to `key`. You can use it to customize how to sort even further. 

Two things to keep in mind.
1. Pass the object without calling it.
2. The function that you pass to `key` must accept only a single argument.

### Usa a Custom Function for Sorting

Can use user defined functions for sorting. 

```python
def get_second_element(item):
    return item[1]

items = [(10, 2), (0, 3), (10, 1)]
items.sort(key=get_second_element)

items # returns list in [(10, 1), (-10, 2), (0, 3)] order
```

This is list method and doesn't work on tuples because they are immutable.
