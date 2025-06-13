matrix = [[1, 2], [3, 4]]

# This creates a second reference to the same object
the_matrix = matrix

# The change affects the object
the_matrix[-1] = ["Neo", "Trinity"]

print(the_matrix)
# [[1, 2], ['Neo', 'Trinity']]
print(matrix)
# [[1, 2], ['Neo', 'Trinity']]
