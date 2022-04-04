#!/usr/bin/env python3

import sys
import string

a = []
for x in sys.stdin:
    x = x.strip().split()
    i = 0
    while i < len(x):
        x[i] = x[i].lower()
        if x[i][-1] in string.punctuation:
            x[i] = x[i].replace(x[i], x[i][:len(x[i]) - 1])
        a.append(x[i])
        i += 1
a = list(dict.fromkeys(a))
print(len(a) - 1)
