#!/usr/bin/env python3

import sys
import collections

def smallest_unique(nr):
    nr = sorted([int(x) for x in nr])
    occurances = collections.Counter(nr)
    if len(occurances) != 1:
        test = min(occurances)
        print(test)
        return '\n'
    else:
        return 'none'


for x in sys.stdin:
    x = x.strip().split()
    print(smallest_unique(x))
