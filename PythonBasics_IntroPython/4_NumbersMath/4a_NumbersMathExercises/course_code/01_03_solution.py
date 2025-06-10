"""
Creating Numbers - Find the Maximum Number

- In IDLE's interactive window, try to find the smallest exponent `N`
  for which `2e<N>`, where `<N>` is replaced with your number,
  returns `inf`.
"""

print(2e308)

import sys
print(sys.float_info.max_10_exp)
