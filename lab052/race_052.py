#!/usr/bin/env python3

import sys
stats = {}
sets = []
def fastest_time(line):
    line = line.strip().split()
    line = line[1:]
    listing = []
    for time in line:
        for character in time:
            is_letter = character.isalpha()
        if is_letter is False:
            time = time.split(":")
            time = ".".join(time)
            time = float(time)
            listing.append(time)
        elif is_letter is True:
            listing.append(0)
    return min(listing)


for runner in sys.stdin:
    name = runner.strip().split()[0]
    time = fastest_time(runner)
    if time != 0:
        sets.append(time)
        stats[time] = name

if min(sets) in stats:
    print(stats[min(sets)], ":", ":".join(str(min(sets)).split(".")))
