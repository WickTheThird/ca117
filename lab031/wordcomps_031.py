#!/usr/bin/env python3

import sys
import collections

check = ["a", 'n', 'g', 'l', 'e']
total = sys.stdin.readlines()
seventeen = []
legal = []
four_a = []
two_q = []
cies = []
angle = []
for x in total:
    counter = 0
    counter_2 = 0
    counter_3 = 0
    x = x.strip()
    if len(x) == 17:
       seventeen.append(x)
    if len(x) >= 18:
       legal.append(x)
    if 'cie' in x:
        cies.append(x)
    if 'a' in x or 'A' in x:
        for y in x:
            if y == 'A' or y == 'a':
                counter += 1
        if counter == 4:
            four_a.append(x)
    if 'q' in x or 'Q' in x:
        for y in x:
            if y == 'q' or y == 'Q':
                counter_2 += 1
        if counter_2 >= 2:
            two_q.append(x)
    n = []
    for y in x.lower():
        n.append(y)
    if collections.Counter(check) == collections.Counter(n) and x != "angle":
        angle.append(x)

print('Words containing 17 letters:', seventeen)
print('Words containing 18+ letters:', legal)
print("Words with 4 a's:", four_a)
print("Words with 2+ q's:", two_q)
print('Words containing cie:', cies)
print('Anagrams of angle:', angle)
