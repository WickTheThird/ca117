#!/usr/bin/env python3

import sys
import collections

def highest_unique(set_nr):
    set_nr = collections.Counter(set_nr.strip().split())
    key = []
    values = []
    if len(set_nr) == 1 or len(set_nr) == 0:
        return 'none'
    else:
        for x in set_nr:
            key.append(x)
            values.append(set_nr[x])
        minimum = min(values)
        key = sorted(key)
        key.reverse()
        for x in key:
            if set_nr[x] == minimum:
                return x


for x in sys.stdin:
    print(highest_unique(x))
