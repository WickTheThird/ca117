#!/usr/bin/env python3

def reverse_list(ordered):
    if ordered != []:
        piece = str(ordered[-1])
        ordered = ordered[:-1]
        return [int(piece)] + reverse_list(ordered)
    return []
