#!/usr/bin/env python3

import sys

prices = sys.stdin.readlines()

def calculate(prices):
    total = 0
    for x in prices:
        total = total + x
    return total

def three_cakes(prices):
    total = 0
    i = 1
    while len(prices) > 4:
        if i % 3 == 0:
            prices.pop(prices.index(min(prices)))
            total = total + calculate(prices[:2])
            prices.pop(0)
            prices.pop(1)
        i += 1
    if len(prices) == 4:
        prices.pop(3)
        for x in prices:
            total = total + x
    elif len(prices) == 3:
        prices.pop(prices.index(min(prices)))
        for x in prices:
            total = total + x
    elif len(prices) < 2 and len(prices) > 0:
        for x in prices:
            total = total + x
    return total


for x in prices:
    x = x.strip().split()
    if len(x) > 2:
        x = [int(y) for y in x]
        print(three_cakes(x))
    else:
        x = [int(y) for y in x]
        print(calculate(x))
