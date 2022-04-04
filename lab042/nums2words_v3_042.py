#!/usr/bin/env python3

import sys
file = sys.argv[1]

words = {'0': 'zero', '1': 'one', '2': "two", '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'}
doc = {}
with open(file) as f:
    f = f.readlines()
    for x in f:
        x = x.strip().split()
        doc[x[0]] = x[1]

for x in sys.stdin:
    x = x.strip().split()
    a = []
    for y in x:
        if y in words:
            a.append(doc[words[y]])
    print(" ".join(a))
