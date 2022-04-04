#!/usr/bin/env python3

def factorial(nr):
    if nr > 1:
        return nr * factorial(nr - 1)
    elif nr == 0:
        return 1
    return nr
