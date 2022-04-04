#!/usr/bin/env python3

import sys
students = sys.argv[1]
a = []
with open(students) as f:
    f = f.readlines()
    for x in f:
        x = x.strip().split()
        try:
            x[0] = int(x[0])
            a.append(x[0])
        except ValueError:
            m = x[0]
            print(f'Invalid mark {m} encountered. Exiting.')
            break
