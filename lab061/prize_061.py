#!/usr/bin.env python3

import sys
import collections

lines = sys.stdin.readlines()
prize = int(lines[0].strip())
swaps = " ".join(lines[1].strip()).split()
positions = [1, 2, 3]

for x in swaps:
    if x == 'A':
        positions[0], positions[1] = positions[1], positions[0]
    elif x == 'B':
        positions[1], positions[2] = positions[2], positions[1]
    elif x == 'C':
        positions[0], positions[2] = positions[2], positions[0]

print(positions.index(prize) + 1)
