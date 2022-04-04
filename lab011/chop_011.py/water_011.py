#!/usr/bin/env python3

import sys
water = sys.stdin.read().strip().split("\n")

buckets = water[1].split()
water = int(water[0].strip())

i = 0
j = 0
while j < len(buckets) and water >= 0:
    x = int(buckets[j])
    if water > 0:
        water = water - x
        i += 1
    j += 1

if j == len(buckets) and i != 9:
    print(i)
else:
    print(i - 1)
