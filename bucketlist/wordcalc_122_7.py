#!/usr/bin/env python3

import sys
variables = {}

def calculator(var_1, opr, var_2):
    if opr == "+":
        return var_1 + var_2
    elif opr == "-":
        return var_1 - var_2

def operator(eq):
    if eq[0] in variables and eq[2] in variables:
        total = calculator(variables[eq[0]], eq[1], variables[eq[2]])
        m = eq[3:]
        i = 0
        while i < len(m) and m[i] != '=':
            if m[i] in '+-' and m[i + 1] in variables:
                total = calculator(total, m[i], variables[m[i + 1]])
            i += 1
        for y in variables:
            if variables[y] == total:
                return " ".join(eq) + " " + y
    return " ".join(eq) + " " + 'unknown'


for x in sys.stdin:
    x = x.strip().split()
    if x[0] == 'def':
        variables[x[1]] = int(x[2])
    elif x[0] == 'calc':
        print(operator(x[1:]))
    elif x[0] == 'clear':
        variables = {}
