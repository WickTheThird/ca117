#!/usr/bin/env python3

class Queue(object):

    def __init__(self):
        self.stuff = []

    def enqueue(self, e):
        self.stuff.append(e)

    def dequeue(self):
        return self.stuff.pop(0)

    def first(self):
        return self.stuff[0]

    def is_empty(self):
        return len(self.stuff) == 0

    def __len__(self):
        return len(self.stuff)
