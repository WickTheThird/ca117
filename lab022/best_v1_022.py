#!/usr/bin/env python3

import sys
students = sys.argv[1]
a = []
with open(students) as f:
    f = f.readlines()
    i = 0
    while i < len(f):
        m = f[i].strip().split()
        a.append(int(m[0]))
        i += 1
    for x in f:
        x = x.strip().split()
        x[0] = int(x[0])
        if max(a) in x:
            print("Best student:", " ".join(x[1:]))
            print("Best mark:", max(a))
            break
