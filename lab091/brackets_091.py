#!/usr/bin/env python3

from gettext import find


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


def matcher(self):
    big = {')': '(', '}': '{', ']': '['}
    small = {'(': ')', '{': '}', '[': ']'}
    this = []
    s = Stack()
    for x in self:
        s.push(x)
    i = 0
    while i < len(self) and (len(self) % 2) == 0:
        if self[i] in small:
            if small[self[i]] in self[i + 1:]:
                this.append(True)
        elif self[i] in big and i != 0:
            if big[self[i]] in self[:i]:
                this.append(True)
        i += 1
    return len(this) == len(self)
