#!/usr/bin/env python3

import sys
def multiples(n):
    return [y for y in range(n + 1) if y % 3 == 0 and y != 0]

def multiples_squared(n):
    return [y * y for y in range(n + 1) if y % 3 == 0 and y != 0]

def multiples_doubled(n):
    return [y * 2 for y in range(n + 1) if y % 4 == 0 and y != 0]

def multiples_or(n):
    return [y for y in range(n + 1) if (y % 3 == 0 or y % 4 == 0) and y != 0]

def multiples_and(n):
    return [y for y in range(n + 1) if (y % 3 == 0 and y % 4 == 0) and y != 0]


for n in sys.stdin:
    print("Multiples of 3:", multiples(int(n.strip())))
    print("Multiples of 3 squared:", multiples_squared(int(n.strip())))
    print("Multiples of 4 doubled:", multiples_doubled(int(n.strip())))
    print("Multiples of 3 or 4:", multiples_or(int(n.strip())))
    print("Multiples of 3 and 4:", multiples_and(int(n.strip())))
