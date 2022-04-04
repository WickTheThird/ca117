#!/usr/bin/env python3

from math import sqrt
import sys

def overlap(*args, **kwargs):
    listy = [0, 0, 1, 0, 0, 1]
    i = 0
    while i < len(args):
        listy[i] = args[i]
        i += 1
    x1 = listy[0]
    y1 = listy[1]
    r1 = listy[2]
    x2 = listy[3]
    y2 = listy[4]
    r2 = listy[5]
    center_1 = (x2 - x1) ** 2
    center_2 = (y2 - y1) ** 2
    d = sqrt(center_1 + center_2)
    if d == 0:
        return True
    elif d == r1 or d == r2:
        return True
    elif (r1 - r2) < d < (r1 + r2):
        return True
    if d == (r1 - r2):
        return True
    else:
        return False
