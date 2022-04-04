#!/usr/bin/env python3

import sys

def sum_factors(nr):
    nr = int(nr.strip())
    factors = []
    for y in range(1, nr):
        if nr % y == 0:
            factors.append(y)
    return factors


for x in sys.stdin:
    numbers = sum_factors(x)
    total = sum(numbers)
    if total == int(x.strip()):
        print(True)
    else:
        print(False)
