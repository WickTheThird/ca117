#!/usr/bin/env python3

def power(nr, pow):
    if pow > 1:
        return nr * power(nr, pow - 1)
    elif pow == 0:
        return 1
    return nr
