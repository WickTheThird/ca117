#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    line = line.strip().split()
    i = 0
    while i < len(line):
        if line[i][0] == "m":
            line[i] = line[i].capitalize()
            i = len(line)
        i += 1
    print(" ".join(line))
