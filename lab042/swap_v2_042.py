#!/usr/bin/env python3

import collections

def swap_unique_keys_values(dict):
    lists = dict.items()
    a = []
    final = {}
    for x in lists:
        a.append(x[1])
    a = collections.Counter(a)
    for y in dict:
        if a[dict[y]] < 2:
            final[dict[y]] = y
    return final
