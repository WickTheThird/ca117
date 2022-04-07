#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()

pattern = words[0].strip()
words = words[1:]

a = []
for x in words:
    x = x.strip()
    if len(x) == len(pattern):
        total = 0
        i = 0
        while i < len(pattern):
            if pattern[i] != '-' and pattern[i] == x[i]:
                total += 1
            elif pattern[i] == '-':
                total += 1
            i += 1
        if total == len(pattern):
            a.append(x)
if len(a) > 0:
    print(', '.join(a).strip())
