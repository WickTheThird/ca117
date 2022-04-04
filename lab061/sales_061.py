#!/usr/bin/env python3

import sys
book = {}
values = []

def average_sale(line):
    line = line.strip().split(":")
    sales = line[-1][1:].split(",")
    total = 0
    i = 0
    while i < len(sales):
        total += int(sales[i])
        i += 1
    return float(total / len(sales))


for x in sys.stdin:
    m = average_sale(x)
    values.append(m)
    x = x.strip().split(":")[0]
    book[m] = x

values = sorted(values)
values.reverse()

for y in values:
    print(f'{book[y]}: {y:.2f}')
