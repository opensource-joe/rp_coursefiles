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


