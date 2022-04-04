#!/usr/bin/env python3

import sys

def mid(s):
    return (len(s) // 2) + 1


for word in sys.stdin:
    s = word.strip()
    middle = mid(s)
    if (len(s) % 2) != 0:
        print(s[middle - 1])
    else:
        print("No middle character!")
