#!/usr/bin/env python3

import sys
li = [i.strip() for i in sys.stdin.readlines()]
print('Words with q but no u:', [x for x in li if 'q' in x.lower().replace("qu", "")])
