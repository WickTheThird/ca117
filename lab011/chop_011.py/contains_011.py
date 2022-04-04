#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()

for x in words:
    word = x.strip().split()
    if len(word[0]) == len(word[1]):
        a = []
        b = []
        for y in word[0]:
            y = y.lower()
            a.append(y)
        for n in word[1]:
            n = n.lower()
            b.append(n)
        for x in a:
            test = []
            i = 0
            while i < len(b):
                if x == b[i]:
                    test.append("True")
                    b.pop(i)
                    i = len(b)
                else:
                    test.append("False")
                i += 1
            if "True" not in test:
                total = "False"
                break
            else:
                total = "True"
        print(total)
    else:
        print(False)
