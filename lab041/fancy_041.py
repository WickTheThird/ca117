#!/usr/bin/env python3

import sys
contacts = sys.argv[1]

contact_dict = {}
with open(contacts) as f:
    f = f.readlines()
    for x in f:
        x = x.strip().split()
        m = " ".join(x[1:])
        contact_dict[x[0]] = m

def check(s):
    s = s.strip()
    if s in contact_dict:
        stuff = contact_dict[s].strip().split()
        print('Name:', s)
        print('Phone:', stuff[0])
        print('Email:', stuff[1])
    else:
        print('Name:', s)
        print('No such contact')


for y in sys.stdin:
    check(y)
