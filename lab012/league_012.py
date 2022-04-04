#!/usr/bin/env pytjon3

import sys
lines = sys.stdin.readlines()
a = []

for x in lines:
    x = x.strip().split()
    nr = "1234567890"
    for n in x[2]:
        if n not in nr:
            x[1] = " ".join(x[1:3])
            x.pop(2)
            break
    for n in x[2]:
        if n not in nr:
            x[1] = " ".join(x[1:3])
            x.pop(2)
            break
    a.append(len(x[1]))

m = max(a)
print(f'{"POS"}' + " " + "CLUB" + " " * ((m - 4) + 2) + f'{"P":4}' + f'{"W":4}' + f'{"D":4}' + f'{"L":3}' + f'{"GF":4}' + f'{"GA":4}' + f'{"GD":3}' + f'{"PTS"}')

for y in lines:
    y = y.strip().split()
    nr = "1234567890"
    for n in y[2]:
        if n not in nr:
            y[1] = " ".join(y[1:3])
            y.pop(2)
            break
    for n in y[2]:
        if n not in nr:
            y[1] = " ".join(y[1:3])
            y.pop(2)
            break
    print(f'{int(y[0]):3d}' + " " + f'{y[1]:{m + 1}}' + f'{int(y[2]):2d}' + f'{int(y[3]):4d}' + f'{int(y[4]):4d}' + f'{int(y[5]):4d}' + f'{int(y[6]):4d}' + f'{int(y[7]):4d}' + f'{int(y[8]):4d}' + f'{int(y[9]):4d}')
