#!/usr/bin/env python3

import sys
def letters(x):
    positions = ""
    final = []
    i = 0
    while i < len(x):
        if x[i] == x[i].lower():
            final.append(positions)
            positions = ""
        if x[i] == x[i].upper():
            positions = positions + str(x[i])
        i += 1
    print(max(final, key=len))


for line in sys.stdin:
    letters(line)
