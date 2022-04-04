#!/usr/bin/env python3

def maximum(nr_list):
    if len(nr_list) > 1:
        if nr_list[0] < nr_list[1]:
            nr_min = nr_list[1]
            nr_list.pop(0)
        elif nr_list[0] > nr_list[1]:
            nr_min = nr_list[0]
            nr_list.pop(1)
        return maximum(nr_list)
    return nr_list[0]
