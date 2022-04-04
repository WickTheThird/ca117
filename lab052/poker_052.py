#!/usr/bin/env python3

import sys
import collections
def poker_strenght(hand):
    hand = hand.strip().split()
    i = 0
    while i < len(hand):
        hand[i] = hand[i][0]
        i += 1
    hand = collections.Counter(hand)
    maximum = []
    for y in hand:
        maximum.append(hand[y])
    return max(maximum)


for cards in sys.stdin:
    print(poker_strenght(cards))
