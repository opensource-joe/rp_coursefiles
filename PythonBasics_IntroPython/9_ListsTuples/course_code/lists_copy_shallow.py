matrix = [[1, 2], [3, 4]]

# This creates a shallow copy of the list
the_matrix = matrix[:]
the_matrix[-1] = ["Neo", "Trinity"]

print(the_matrix)
# [[1, 2], ['Neo', 'Trinity']]
print(matrix)
# [[1, 2], [3, 4]]
