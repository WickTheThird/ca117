#!/usr/bin/env python3

import sys

def chop(s):
    return s[1:len(s) - 1]


for line in sys.stdin:
    if len(line.strip()) > 1:
        line_1 = line[0].strip()
        line_2 = line[-2].strip()
        s = line.strip()
        chopped = line_1.upper() + chop(s) + line_2.upper()
        if len(chopped) > 0:
            print(chopped)
