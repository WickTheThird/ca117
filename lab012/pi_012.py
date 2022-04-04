#!/usr/bin/env python3

import sys
from math import pi

for i in sys.stdin:
   print(f'{pi:.{int(i)}f}')
