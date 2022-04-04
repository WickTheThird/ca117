#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(
            self.x, self.y
        )

class Circle(object):

    def __init__(self, point=None, rad=1):
        if point is None:
            self.centre = Point(0, 0)
            self.radius = rad
        elif point is not None:
            self.centre = point
            self.radius = rad

    def __str__(self):
        return 'Cent: {}\nRadius: {}'.format(
            self.centre, self.radius
        )
