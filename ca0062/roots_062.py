#!/usr/bin/env python3

import sys
from math import sqrt

for x in sys.stdin:
    x = x.strip().split()
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    try:
        r1 = ((-1) * b + sqrt((b ** 2) - 4 * a * c)) / (2 * a)
        r2 = ((-1) * b - sqrt((b ** 2) - 4 * a * c)) / (2 * a)
        print('r1 =', str(r1) + ',', 'r2 =', r2)
    except ValueError:
        print(None)
