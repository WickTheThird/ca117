#!/usr/bin/env pyhton3

import sys

def plural(s):
    con = "bcdfghjklmnpqrstvwxz"
    voc = "aeiou"
    if s[len(s) - 2:] == "ch" or s[len(s) - 2:] == "sh" or s[-1] == "s" or s[-1] == "z" or s[-1] == "x":
        print(s + "es")
    elif s[len(s) - 2: -1] in con and s[-1] == "y":
        print(s[:len(s) - 1] + "ies")
    elif s[-1] == "f":
        print(s[:len(s) - 1] + "ves")
    elif s[len(s) - 2:] == "fe":
        print(s[:len(s) - 2] + "ves")
    elif s[-1] == "o":
        print(s[:len(s)] + "es")
    else:
        print(s + "s")


for word in sys.stdin:
    plural(word.strip())
