#!/usr/bin/env python3

import collections
import sys
lines = " ".join(sys.stdin.readlines())
letters = []
[letters.append(x.lower()) for x in lines]
occurances = collections.Counter(letters)
numbers = []
final = {}
for y in occurances:
    if y in 'aeiou':
        final[occurances[y]] = y
        numbers.append(int(occurances[y]))

numbers = sorted(numbers)
numbers.reverse()

for z in numbers:
    print(final[z], ":", f'{z:{len(str(max(numbers)))}d}')
