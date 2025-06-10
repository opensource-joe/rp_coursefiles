"""
Formatting Numbers - Limit Decimal Places

- Print the result of the calculation `3 ** .125` as a fixed-point number
  with three decimal places.
"""

print(f"{3 ** .125:.3f}")
print(format(3 ** .125, ".3f"))
print("{:.3f}".format(3 ** .125))
