#!/usr/bin/env python3

import sys
import collections

def check_nice(word):
    letters = " ".join(word).split()
    word = collections.Counter(letters)
    test = ['n', 'i', 'c', 'e']
    listings = []
    for x in letters:
        if x == 'n' or x == 'i' or x == 'c' or x == 'e':
            if word[x] == 1:
                listings.append(x)
    if listings == test:
        print("".join(letters))


for x in sys.stdin:
    check_nice(x)
