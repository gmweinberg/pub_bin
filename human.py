#!/usr/bin/env python
import sys

"""print human-readable numbers"""

if __name__ == '__main__':
    num = int(sys.argv[1])
    if num > 10**9:
        print(str(round(num/10**9, 3)) + "G")
    elif num > 10**6:
        print(str(round(num/10**6, 3)) + "M")
    elif num > 10**3:
        print(str(round(num/10**3, 3)) + "K")
    else:
        print(num)

