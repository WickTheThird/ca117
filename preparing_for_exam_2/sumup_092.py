#!/usr/bin/env python3

def sumup(nr):
    if nr > 1:
        return nr + sumup(nr - 1)
    return nr
