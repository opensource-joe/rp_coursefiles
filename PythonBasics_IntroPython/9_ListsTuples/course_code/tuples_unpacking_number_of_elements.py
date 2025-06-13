# The number of variable names must match
# the number of elements in the tuple

a, b, c = 1, 2  # ValueError

a, b = 1, 2, 3  # ValueError
