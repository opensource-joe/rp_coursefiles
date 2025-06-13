# Return multiple values wrapped in a tuple
def get_stats(sequence):
    return max(sequence), min(sequence)


numbers = (1, 2, 3)
print(get_stats(numbers))

# Unpack the tuple return value
maximum, minimum = get_stats(numbers)
print(maximum)
print(minimum)
