# Display every number from 1 through 50 except multiples of 3

for number in range(1, 51):
    # except multiples of 3
    if number % 3 == 0:
        continue
    print(number)
