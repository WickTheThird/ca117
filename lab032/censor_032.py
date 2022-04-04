#!/usr/bin/env python3

import sys
file_1 = sys.argv[1]
with open(file_1) as f:
    f = f.readlines()

def censor(s):
    s = s.strip().split()
    for x in f:
        i = 0
        x = x.strip().split()
        for y in s:
            i += 1
            if x[0] in y:
                y = y.replace(x[0], '@' * len(x[0]))
                s[i - 1] = y
    print(' '.join(s))


verse = 0
for x in sys.stdin:
    if censor(x) is not None:
        print(censor(x))
