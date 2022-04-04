#!/usr/bin/env python3

import sys
contacts = sys.argv[1]

contact_dict = {}
with open(contacts) as f:
    f = f.readlines()
    for x in f:
        x = x.strip().split()
        contact_dict[x[0]] = x[1]

def check(s):
    s = s.strip()
    if s in contact_dict:
        print("Name:", s)
        print("Phone:", contact_dict[s])
    else:
        print('Name:', s)
        print('No such contact')


for y in sys.stdin:
    check(y)
