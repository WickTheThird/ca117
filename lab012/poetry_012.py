#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()
n = []

for y in words:
    m = len(y.strip())
    n.append(m)

for x in words:
    m = max(n)
    x = x.rstrip()
    print(f'{x:^{m}}')
