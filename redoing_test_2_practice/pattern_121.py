#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
pattern = lines[0].strip()
lines = [x.strip() for x in lines[1:]]

words = []

for x in lines:
    find_p = []
    if len(x) == len(pattern):
        for i, y in enumerate(pattern):
            if x[i] == y:
                find_p.append(x[i])
            elif y == '-':
                find_p.append(y)
        if ''.join(find_p) == pattern:
            words.append(x)

if len(words) > 0:
    print(', '.join(words))
