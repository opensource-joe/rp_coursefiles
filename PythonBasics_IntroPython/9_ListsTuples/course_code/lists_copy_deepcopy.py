import copy

matrix = [[1, 2], [3, 4]]

# This creates a deep copy (true copy) of all nested elements
the_matrix = copy.deepcopy(matrix)
the_matrix[0][0] = "The Oracle"

print(the_matrix)
# [["The Oracle", 2], [3, 4]]
print(matrix)
# [[1, 2], [3, 4]]
