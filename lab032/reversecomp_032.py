#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
list_a = []
list_b = []
[list_a.append(x.strip().lower()) for x in lines if len(x.strip()) >= 5]
[list_b.append(x.strip()) for x in lines if len(x.strip()) >= 5]
a = []
def sherlock(query, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] < query:
            low = mid + 1
        elif sorted_list[mid] > query:
            high = mid - 1
        else:
            return mid
    return False


for x in list_a:
    x = x.strip().lower()[::-1]
    testing = sherlock(x, list_a)
    if testing is not False:
        a.append(list_b[testing])
print(sorted(a, key=str.casefold))
