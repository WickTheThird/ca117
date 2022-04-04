#!/usr/bin/env python3

import numbers
import sys
def replace(n):
    umbers = []
    for y in range(n + 1):
        if y != 0 and y % 3 != 0:
            umbers.append(y)
        elif y != 0 and y % 3 == 0:
            umbers.append('X')
    return umbers


for x in sys.stdin:
    print('Multiples of 3 replaced:', replace(int(x.strip())))
