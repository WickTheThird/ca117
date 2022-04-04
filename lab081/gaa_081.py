#!/usr/bin/env python3

class Score(object):

    def __init__(self, x=0, y=0):
        self.goals = x
        self.points = y

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(
            self.goals, self.points
        )
