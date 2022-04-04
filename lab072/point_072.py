#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, point):
        return (((point.x - self.x) ** 2) + ((point.y - self.y) ** 2)) ** (1 / 2)

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(
            self.x, self.y
        )
