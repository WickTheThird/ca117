#!/usr/bin/env python3

import sys
variables = {}
check = {}

def calculate(eq):
    total = 0
    if eq[1] == "+" and eq[0] in variables and eq[2] in variables:
        total = variables[eq[0]] + variables[eq[2]]
    elif eq[1] == "-" and eq[0] in variables and eq[2] in variables:
        total = variables[eq[0]] - variables[eq[2]]
    m = eq[3:]
    i = 0
    while (i + 1) < len(m) and m[i] != '=' and len(m) > 1:
        if m[i] == "+" and m[i + 1] in variables:
            total = total + variables[m[i + 1]]
        elif m[i] == "-" and m[i + 1] in variables:
            total = total - variables[m[i + 1]]
        i += 1
    if total in check:
        return " ".join(eq) + " " + check[total]
    return " ".join(eq) + " " + 'unknown'


for x in sys.stdin:
    if x.lower().strip().split()[0] == 'def':
        variables[x.lower().strip().split()[1]] = int(x.lower().strip().split()[2])
        check[int(x.lower().strip().split()[2])] = x.lower().strip().split()[1]
    elif x.lower().strip().split()[0] == 'calc':
        print(calculate(x.lower().strip().split()[1:]))
    elif x.lower().strip().split()[0] == 'clear':
        variables = {}
        check = {}
