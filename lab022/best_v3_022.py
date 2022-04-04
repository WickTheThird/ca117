#!/usr/bin/env python3

from operator import index
import sys
students = sys.argv[1]
a = []
b = []
i = 1
with open(students) as f:
    f = f.readlines()
    for x in f:
        x = x.strip().split()
        a.append(x[0])
        b.append(" ".join(x[1:]))
for y in a:
    try:
        y = int(y)
        i += 1
    except ValueError:
        print(f'Invalid mark {y} encountered. Skipping.')
print('Best student:', b[a.index(max(a))])
print('Best mark:', max(a))
