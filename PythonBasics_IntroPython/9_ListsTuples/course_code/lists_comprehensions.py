numbers = (1, 2, 3)

# Using a for loop
squares_1 = []
for num in numbers:
    squares_1.append(num**2)

print(squares_1)

# Using a list comprehension
squares_2 = [num**2 for num in numbers]

print(squares_2)
print(type(squares_2))
