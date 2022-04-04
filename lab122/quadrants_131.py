#!/usr/bin/env python3

import sys

def quadrant(numbers):
    if '-' not in numbers[0] and '-' not in numbers[1]:
        return 1
    elif '-' in numbers[0] and '-' not in numbers[1]:
        return 2
    elif '-' in numbers[0] and '-' in numbers[1]:
        return 3
    if '-' not in numbers[0] and '-' in numbers[1]:
        return 4


for x in sys.stdin:
    print(quadrant(x.strip().split()))
