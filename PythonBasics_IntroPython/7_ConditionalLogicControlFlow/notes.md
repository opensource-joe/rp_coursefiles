# Python Basics: Conditional Logic and Control Flow
https://realpython.com/courses/basics-conditional-logic-control-flow/

## Adding Some Logic to Your Code

Conditional logic allows you to check if something is true or false. Use the following.
- Boolean comparators
- Conditional statements
- Logical operators
- Operator precedence

Boolean comparators are used for comparing values.
- ">" greater than
- "<" less than
- ">=" greater than or equal to
- "<=" less than or equal to
- "!=" not equal to
= "==" equal to

Conditional statements. These are all True.
- 10 > 5
- 1 < 2
- 10 >= 9
- 5 <= 5
- 1 != 0
- 100 == 100

These are all False.
- 10 < 5
- 1 > 2
- 10 <= 9
- 4 >= 5
- 1 == 0
- 100 != 100

Logical operators. Evaluated as boolean.
- and - need value on both sides. Only return True when both sides are True.
- or - need value on both sides. Only case when False is when both sides are False.
- not - only need value on one side. Invert the value. Not False is True, Not True is False.

Operator precedence.
- Boolean comparators are first to evaluate. <, <=, ==, !=, >=, >
- not
- and
- or
- Can work around this behavior by using brackets. Whatever is in brackets operates first. Break up statements to evaluate if needed.
- When working with strings, precedence by alphabetical order. "a" has less value than "z".

## Building Complex Expressions

- 1 != 1: False
- not False: True
- True and True: True
- ("a" != "a") or not (2 >= 3): True

## Controlling the Flow of Your Program

Create branches - a program can contain many branches but you want to keep to a minimum for coming back to code and simplicity.
- if
- else
- elif
- if ... elif ... else

---

if Keyword.

    if [condition]:
       ...
    print("done")

The key is that anything in the indented block will only run if the condition is True. Anything not indented, is outside if construct, will always run no matter the condition.

    if True:
        print("Hello!")
   
    if False:
        print("Hello!")
    
    print("done")

Grading example.

```python
grade = 100

if grade >= 50:
    print("You passed")

print("Grading done.")
```

---

Else keyword.

    if [condition]:
        ...
    else
        ...

Else keyword linked to original If statement. If condition is False, Else block will run.

```python
grade = 100

if grade = 100:
    print("You passed")
else
    print("You failed")
```

---

Elif keyword.

    if [keyword]:
        ...
    elif [condition]:
        ...
    else:
        ...

Elif takes a condition and behaves like an If condition. If it evaluates to True then it runs the indented block. The special thing about Elif is that you can have many of them between If and Else. Only one If and one Else per structure. When Elif evaluates to True then that one will run and none of the others. Tests each one by one, once it reaches first True then it executes and doesn't matter what comes after.

```python
""" A: 70+
    B: 60-69
    C: 50-59
    F: less than 50
"""
grade = 40

if grade >= 70:
    print("You did great!")
elif grade >= 60:
    print("In the 60s")
elif grade >= 50:
    print("In the 50s")
else:
    print("Less than 50")
```

## Creating Nested If Statements

Example: Evaluate the Winner
- Two people play either basketball or golf.
- They tell you what sport they have been playing and their score.
- You have to evaluate who won.
- In golf, the lower score wins. In basketball, the higher score wins.

```python
sport = "golf"
p1_score = 1
p2_score = 9

if p1_score == p2_score:
    print("It's a draw!")

elif sport == "golf":
    if p1_score < p2_score:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

elif sport == "basketball":
    if p1_score > p2_score:
        ("Player 1 wins!")
    else:
        print("Player 2 wins!")

else:
    print("Unknown sport!")
```

Python says flat is better than nested. Can simplify or flatten with refactoring.

## Breaking Out of the Pattern

- Bringing loops into the mix.

```python
sum_of_events = 0

for n in range(10):
    if n % 2 == 0: #check to see if number is evenly divisible
        sum_of_evens = sum_of_evens + n

print(sum_of_events)
```

- Using the Break keyword. Use to stop While loop from running forever.

```python
for n in range(4):
    if n == 2: 
        break
    print(n)
```

- Using the Continue keyword. Will continue printing 2 and then the numbers that follow.

```python
for n in range(4):
    if n == 2:
        print("there goes two")
        continue
    print(n)
```

```python
n = 0

while True:
    print(n)
    if n < 5:
        n = n + 1
        continue
    else:
        break
    print("end of loop")

```

## Recovering From Errors

Types of errors and exceptions.
- SyntaxError
    - ValueError
    - TypeError
    - NameError
    - ZeroDivisionError
    - OverflowError

## Using the Try and Except Keywords

Use the Try...Except structure to handle exceptions gracefully.

```python
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That was not an integer")
```

```python
def divide(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Both arguments must be numbers")
    except ZeroDivisionError:
        print("num2 must not be 0")
```

## Simulating and Calculating Probabilities

Use the random module, simulate many coin tosses, calculate the ratio of heads to tails, and alter the behavior of the coin.

    import random
    random.randint(1, 10)

```python
import random

def coin_flip():
    # randomly return 'heads' or 'tails'
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails" 

for i in range(10):
    print(coin_flip())
```

Unfair coins. Replace coin_flip() with this for probability.

```python
import random

def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"
```

```python
heads_tally = 0
tails_tally = 0

for trial in range(10_000):
    if coin_flip() == "heads":
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

print("heads", heads_tally)
print("tails", tails_tally)
```

### Quiz
1. Write a Python if … else statement in the code box below that sets the variable m to the smaller of a and b.

```python
a = 100
b = 50

if a < b:
    m = a
else:
    m = b
```