matrix = [[1, 2], [3, 4]]

# This creates a shallow copy of the list
the_matrix = matrix[:]

# Shallow copies contain references to objects
the_matrix[0][0] = "Morpheus"

print(the_matrix)
# [["Morpheus", 2], [3, 4]]
print(matrix)
# [["Morpheus", 2], [3, 4]]
