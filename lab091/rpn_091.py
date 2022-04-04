#!/usr/bin/env

from math import sqrt

class Stack(object):

    def __init__(self):
        self.stuff = []

    def push(self, e):
        self.stuff.append(e)

    def pop(self):
        return self.stuff.pop()

    def top(self):
        return self.stuff[-1]

    def is_empty(self):
        return len(self.stuff) == 0

    def __len__(self):
        return len(self.stuff)


def calculator(self):
    binops = {'+': float.__add__, '-': float.__sub__, '*': float.__mul__, '/': float.__truediv__}
    uniops = {'n': float.__neg__, 'r': sqrt}
    opr = []
    s = Stack()
    self = self.split()
    for x in self:
        if x not in binops and x not in uniops:
            s.push(float(x))
        else:
            opr.append(x)
    total = 0
    if len(opr) > 0 and len(s.stuff) > 1 and opr[0] in binops:
        total = binops[opr[0]](s.stuff[-2], s.top())
        s.pop()
        s.pop()
        opr.pop(0)
    elif len(opr) > 0 and len(s.stuff) > 1 and opr[0] in uniops:
        total = uniops[opr[0]](s.top())
        s.pop()
        opr.pop(0)
    elif len(s.stuff) == 1 and len(opr) == 1 and opr[0] in uniops:
        total = uniops[opr[0]](s.top())
        s.pop()
        opr.pop(0)
    elif len(opr) == 0:
        total = s.stuff[0]
        s.pop()
    elif len(opr) == 1 and len(s.stuff) >= 1:
       return opr[100]
    i = 0
    while i < len(opr):
        if opr[i] in binops:
            total = binops[opr[i]](s.top(), total)
            s.pop()
        elif opr[i] in uniops and opr[i] != 'r':
            total = uniops[opr[i]](total)
        elif opr[i] == 'r':
            total = total ** (1 / 2)
        i += 1
    return total
