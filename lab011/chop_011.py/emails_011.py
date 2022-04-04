#!/usr/bin/env python3

import sys
import re

pattern = r'[0-9]'

for x in sys.stdin:
    name = x.strip().split("@")
    name = name[0].split(".")
    i = 0
    while i < len(name):
        name[i] = re.sub(pattern, "", name[i]).capitalize()
        i += 1
    name = " ".join(name)
    print(name)
