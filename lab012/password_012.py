#!/usr/bin/env python3

import sys

def check(s):
    res = 0
    res_2 = 0
    res_3 = 0
    res_4 = 0
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUBVWXYZ"
    n = "1234567890"
    for char in s:
        if str(char) in low:
           res = 1
        elif str(char) in up:
           res_2 = 1
        elif str(char) in n:
            res_3 = 1
        elif str(char) not in (low or up or n) and str(char) != " ":
            res_4 = 1
    return res + res_2 + res_3 + res_4


for x in sys.stdin:
   m = check(x.strip())
   print(m)
