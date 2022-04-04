#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
n = [0] * 3
nums = lines[0].strip().split()
patterns = lines[1].strip()
i = 0
while i < len(nums):
    nums[i] = int(nums[i])
    i += 1
a = patterns.index('A')
b = patterns.index('B')
c = patterns.index('C')
n[a] = str(min(nums))
nums.pop(nums.index(min(nums)))
n[c] = str(max(nums))
nums.pop(nums.index(max(nums)))
n[b] = str(nums[0])
print(' '.join(n))
