#!/usr/bin/env python3

import sys
this = {}

def counting(line):
    line = line.strip().split()
    i = 0
    while i < len(line):
        if ',' in line[i] or '.' in line[i] or '?' in line[i] or '!' in line[i] or ':' in line[i]:
            line[i] = line[i][:-1]
        line[i] = line[i].lower()
        if line[i] not in this:
            this[line[i]] = [i]
        elif line[i] in this:
            this[line[i]].append(i)
        i += 1
    return this

def test(word, the_list):
    word = word.lower()
    if ',' in word or '.' in word or '?' in word or '!' in word or ':' in word:
        word = word[:-1].lower()
    if word in this and len(this[word]) > 1:
        this[word].pop(0)
        the_list[this[word][0]] = '.'


for x in sys.stdin:
    this = counting(x)
    x = x.split()
    for y in x:
        test(y, x)
    print(' '.join(x))
