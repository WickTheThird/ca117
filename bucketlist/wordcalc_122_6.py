#!/usr/bin/env python3

import sys
variables = {}
values = {}

def calculator(var_1, opr, var_2):
    if opr == "+":
        return var_1 + var_2
    elif opr == "-":
        return var_1 - var_2

def calc_res(eq):
    total = 0
    if eq[0] in variables and eq[2] in variables:
        total = calculator(variables[eq[0]], eq[1], variables[eq[2]])
    m = eq[3:]
    i = 0
    while i < len(m) and m[i] != '=' and len(m) > 1:
        if m[i] in '+-' and m[i + 1] in variables:
            total = calculator(total, m[i], variables[m[i + 1]])
        i += 1
    if total in values:
        return " ".join(eq) + " " + values[total]
    return " ".join(eq) + " " + 'unknown'


for x in sys.stdin:
    x = x.strip().lower().split()
    if x[0] == 'def':
        variables[x[1]] = int(x[2])
        values[int(x[2])] = x[1]
    elif x[0] == 'calc':
        print(calc_res(x[1:]))
    elif x[0] == 'clear':
        variables = {}
        values = {}
