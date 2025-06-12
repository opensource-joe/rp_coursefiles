def print_total():
    def inner_print_total():
        print(f"From inner function: {total=}")

    total = 0
    inner_print_total()
    print(f"From function: {total=}")

print_total()
