#!/usr/bin/env python3

def count_letters(n):
    if n == '':
        return 0
    return 1 + count_letters(n[1:])
