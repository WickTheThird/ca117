#!/usr/bin/env python3

import sys

for x in sys.stdin:
    final = ''
    x = x.strip()
    i = 0
    while i < len(x):
        if x[i] in 'aeiou':
            final = final + x[i]
            i += 2
        elif x[i] not in 'aeiou':
            final = final + x[i]
        i += 1
    print(final)
