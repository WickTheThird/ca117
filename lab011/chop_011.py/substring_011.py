#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()

for x in words:
    new = x.strip().split()
    new[0] = new[0].lower()
    new[1] = new[1].lower()
    print(new[0] in new[1])
