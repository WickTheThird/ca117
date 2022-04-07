#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao
        self.total = {}
        self.points = []

    def add_grade(self, type, grade):
        self.total[type] = grade
        point = holder[grade]
        self.points.append(point)

    def get_grade(self, type):
        if type in self.total:
            return self.total[type]
        return 'N/A'

    def __str__(self):
        point_high = sorted(self.points, reverse=True)
        i = 0
        point_print = 0
        if len(point_high) < 4:
            for item in point_high:
                point_print += item
        else:
            while i < 3:
                point_print += point_high[i]
                i += 1
        return 'Name: {}\nCAO: {}\nPoints: {}'.format(self.name, self.cao, point_print)


holder = {'H1': 100, 'H2': 88, 'H3': 77, 'H4': 66, 'H5': 56, 'H6': 46, 'H7': 37, 'H8': 0, 'O1': 56, 'O2': 46, 'O3': 37, 'O4': 28, 'O5': 20, 'O6': 12, 'O7': 0, 'O8': 0}
