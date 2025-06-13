def get_second_element(item):
    return item[1]


items = [(-10, 2), (0, 3), (10, 1)]

items.sort(key=get_second_element)
print(items)
# [(10, 1), (-10, 2), (0, 3)]
