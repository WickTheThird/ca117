#!/usr/bin/env python3

def fibonacci(nr):
    if nr > 1:
        return fibonacci(nr - 1) + fibonacci(nr - 2)
    return 1
