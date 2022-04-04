#!/usr/bin/env python3

def swap_keys_values(dict):
    lists = dict.items()
    new_dict = {}
    for x in lists:
        new_dict[x[1]] = x[0]
    return new_dict
