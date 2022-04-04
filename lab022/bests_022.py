#!/usr/bin/env python3

import sys
students = sys.argv[1]
a = []
b = []
total = ""
with open(students) as f:
    f = f.readlines()
    for x in f:
        x = x.strip().split()
        a.append(int(x[0]))
        b.append(" ".join(x[1:]))

positions = [i for i, x in enumerate(a) if x == max(a)]
for x in positions:
   total = total + ", " + b[x]

total = total[2:]
print('Best student(s):', total)
print('Best mark:', max(a))
