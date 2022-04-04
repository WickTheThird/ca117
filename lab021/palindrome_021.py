#!/usr/bin/env python3

import sys
for s in sys.stdin.readlines():
    x = list(''.join(e for e in s if e.isalnum()).lower())
    is_a_palindrome = True
    while len(x) > 1:
        w1 = x.pop()
        w2 = x.pop(0)
        if w1 != w2:
            is_a_palindrome = False
            break
    print(is_a_palindrome)
