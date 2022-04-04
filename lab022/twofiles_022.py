#!/usr/bin/env pyhton3

import sys
file_1 = sys.argv[1]
file_2 = sys.argv[2]

with open(file_1) as f:
    list = f.readlines()

with open(file_2) as f_2:
    list_2 = f_2.readlines()

i = 0
while i < len(list):
    print(list[i].strip())
    print(list_2[i].strip())
    i += 1
