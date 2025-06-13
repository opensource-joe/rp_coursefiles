# Lists are similar to tuples in some ways:
numbers = [1, 2, 3, 4]

# Indexing
print(numbers[1])

# Slicing
print(numbers[1:3])

# Membership testing
print(2 in numbers)
print("Bob" in numbers)

# Iterating
for number in numbers:
    if number % 2 == 0:
        print(number)
