#!/usr/bin/env python3

import sys
import calendar

poem = "Monday's child is fair of face.\nTuesday's child is full of grace.\nWednesday's child is full of woe.\nThursday's child has far to go.\nFriday's child is loving and giving.\nSaturday's child works hard for a living.\nSunday's child is fair and wise and good in every way."
week = "Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday"
week = week.split("\n")
poem = poem.split("\n")

for x in sys.stdin:
    x = x.strip().split()
    day = int(x[0])
    month = int(x[1])
    year = int(x[2])
    m = calendar.weekday(year, month, day)
    print("You were born on a " + week[m] + " and " + poem[m])
