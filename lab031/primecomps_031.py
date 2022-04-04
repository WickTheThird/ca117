#!/usr/bin/env python3

import sys
def prime(n):
    primes = []
    for y in range(n + 1):
        if y != 1 and (y == 3 or y == 2 or y == 5 or y == 7):
            primes.append(y)
        elif y % 5 != 0 and y % 3 != 0 and y % 2 != 0 and y != 1 and y % 7 != 0:
            primes.append(y)
    return primes


for x in sys.stdin:
    print('Primes:', prime(int(x.strip())))
