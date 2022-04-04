#!/usr/bin/env python3

import sys

variables = {}

def calculation(eq):
    pass

for x in sys.stdin:
    x = x.strip().lower().split()
    if x[0] == 'def':
        variables[x[1]] = int(x[2])
    elif x[0] == 'calc':
        print(calculation[x[1:]])
    elif x[0] == 'clear':
        variables = {}
