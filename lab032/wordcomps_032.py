#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
words = ''
a = []
b = []
c = []
vowels = ['a', 'e', 'i', 'o', 'u']
def vowel(s):
    total = 0
    m = [x for x in s.lower() if x in vowels]
    m = sorted("".join(m))
    if m == vowels:
        a.append(len(s))
    else:
        a.append(100)
    if s[len(s) - 4:] == "iary":
        b.append(s)
    for y in s:
        if y == 'e':
            total += 1
    c.append(total)


for x in lines:
    x = x.strip()
    vowel(x)

print('Shortest word containing all vowels:', lines[a.index(min(a))].strip())
print('Words ending in iary:', len(b))
maximum = max(c)
i = 0
while i < len(c):
    if c[i] == maximum:
         words = words + " " + lines[i].strip()
    i += 1
words = words.strip().split()
print("Words with most e's:", words)
