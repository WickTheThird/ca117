#!/usr/bin/env python3

def minimum(n):
    if len(n) == 2:
        if n[0] < n[1]:
            return n[0]
        else:
            return n[1]
    else:
        x = minimum(n[1:])
        if n[0] < x:
            return n[0]
        else:
            return x
