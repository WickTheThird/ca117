#!/usr/bin/env python3

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
