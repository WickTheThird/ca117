#!/usr/bin/env python3

import sys
variables = {}

def equation(lines):
    global variables
    for word in lines:
        if word not in variables and word not in "+-=":
            return " ".join(lines) + " " + 'unknown'
    values = [x for x in lines if x not in "+-="]
    signs = [y for y in lines if y in '+-=']
    if signs[0] == "+":
            total = int(variables[values[0]]) + int(variables[values[1]])
    elif signs[0] == "-":
        total = int(variables[values[0]]) - int(variables[values[1]])
    signs = signs[1:]
    values = values[2:]
    i = 0
    while i + 1 < len(signs) and signs != "=" and len(values) > 0:
        if signs[i] == "+":
            total = total + int(variables[values[i]])
        elif signs[i] == "-":
            total = total - int(variables[values[i]])
        i += 1
    for z in variables:
        if str(variables[z]) == str(total):
            return " ".join(lines) + " " + z
    return " ".join(lines) + " " + 'unknown'


for x in sys.stdin:
    x = x.strip().lower().split()
    if x[0] == 'def':
        variables[x[1]] = x[2]
    elif x[0] == 'calc':
       print(equation(x[1:]))
    elif x[0] == 'clear':
        variables = {}
