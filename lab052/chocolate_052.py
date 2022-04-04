#!/usr/bin/env python3

import sys
import math
for line in sys.stdin:
    line = round(int(line.strip()) / 400)
    print(line)
