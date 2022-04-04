#!/usr/bin/env python3

import sys
words = {'0': 'zero', '1': 'one', '2': "two", '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'}

for x in sys.stdin:
    x = x.strip().split()
    a = []
    for y in x:
        if y in words:
            a.append(words[y])
        else:
            a.append('unknown')
    print(' '.join(a))
