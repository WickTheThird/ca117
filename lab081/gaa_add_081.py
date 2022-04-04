#!/usr/bin/env python3

class Score(object):

    def __init__(self, x=0, y=0):
        self.goals = x
        self.points = y
        self.score = x * 3 + y

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __eq__(self, other):
        return self.score == other.score

    def __ne__(self, other):
        return self.score != other.score

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score

    def __add__(self, other):
        goals = self.goals + other.goals
        points = self.points + other.points
        return Score(goals, points)

    def __iadd__(self, other):
        self.goals += other.goals
        self.points += other.points
        return self

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(
            self.goals, self.points
        )
