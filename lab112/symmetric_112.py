#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
all = {}

def one_way(names):
    for x in names:
        if len(x) > 0:
            print(x.strip())
        else:
            m = 0

def other_way(names):
    this = [names[x].strip() for x in names]
    i = 0
    while i < len(this):
        m = this[len(this) - 1 - i]
        if len(m) > 0:
            print(m.strip())
        else:
            m = 0
        i += 1


i = 0
while (i + 1) < len(lines):
    lines[i] = lines[i].strip()
    if i == 0 or i % 2 == 0:
        all[lines[i].strip()] = lines[i + 1]
    i += 1

if len(lines) % 2 != 0:
    all[lines[-1]] = ''

one_way(all)
other_way(all)
