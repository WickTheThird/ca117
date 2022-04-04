#!/usr/bin/env python3

import sys
variables = {}

def operator(var_1, opr, var_2):
    if opr == "+":
        return var_1 + var_2
    elif opr == "-":
        return var_1 - var_2

def calculator(eq):
    if eq[0] in variables and eq[2] in variables:
        total = operator(variables[eq[0]], eq[1], variables[eq[2]])
        m = eq[3:]
        i = 0
        while m[i] != "=" and len(m) > 1:
            if m[i + 1] in variables:
                total = operator(total, m[i], variables[m[i + 1]])
            i += 1
        if total in variables:
            return " ".join(eq) + " " + variables[total]
    return " ".join(eq) + " " + "unknown"


for x in sys.stdin:
    x = x.strip().split()
    if x[0] == 'def':
        variables[x[1]] = int(x[2])
        variables[int(x[2])] = x[1]
    elif x[0] == 'calc':
        print(calculator(x[1:]))
    elif x[0] == 'clear':
        variables = {}
