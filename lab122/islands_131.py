#!/usr/bin/env python3

import sys

islands = {}

def plot(points):
    if points[0] not in islands and points[1] not in islands:
        man = False
        for x in islands:
            ch1 = set(points[0]).issubset(set(islands[x]))
            ch2 = set(points[1]).issubset(set(islands[x]))
            if ch1 is True and ch2 is True:
                man = False
            if ch1 is True and ch2 is False:
                islands[x].append(points[1])
                man = False
            if ch1 is False and ch2 is True:
                islands[x].append(points[0])
                man = False
            if ch1 is False and ch2 is False:
                man = True
        if len(islands) == 0:
            islands[points[0]] = [points[1]]
        if man is True:
            islands[points[0]] = [points[1]]
    elif points[0] in islands or points[1] in islands:
        islands[points[0]].append(points[1])


for x in sys.stdin:
    x = x.strip().split()
    if len(x) > 1:
        plot(x)

print(len(islands))
