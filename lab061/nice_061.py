#!/usr/bin/env python3

import sys
import collections

def check_nice(word):
    letters = " ".join(word).split()
    word = collections.Counter(letters)
    total = 0
    for x in letters:
        if x == 'n' or x == 'i' or x == 'c' or x == 'e':
            if word[x] == 1:
                total += 1
    if total == 4:
        print("".join(letters))


for x in sys.stdin:
    check_nice(x)
