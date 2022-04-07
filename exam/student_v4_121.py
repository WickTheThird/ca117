#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.agenda = {}
        self.points_h = {'H1': 100, 'H2': 88, 'H3': 77, 'H4': 66, 'H5': 56, 'H6': 46, 'H7': 37, 'H8': 0}
        self.points_o = {'O1': 56, 'O2': 46, 'O3': 37, 'O4': 28, 'O5': 20, 'O6': 12, 'O7': 0, 'O8': 0}
        self.name = name
        self.cao = cao

    def add_grade(self, course, grade='N/A'):
        self.agenda[course] = grade

    def get_grade(self, course):
        if course in self.agenda:
            for x in self.agenda:
                if x == course:
                        return self.agenda[course]
        else:
            return 'N/A'

    def __add__(self):
        if len(self.agenda) > 0:
            total = 0
            i = 0
            for x in self.agenda:
                if self.agenda[x] in self.points_h:
                    total = total + self.points_h[self.agenda[x]]
                    i += 1
                if i == 3:
                    return total
            for x in self.agenda:
                if self.agenda[x] in self.points_o:
                    total = total + self.points_o[self.agenda[x]]
                    i += 1
                if i == 3:
                    return total
            return total
        return 0

    def __eq__(self, other):
        return self.__add__() == other.__add__()

    def __lt__(self, other):
        return self.__add__() < other.__add__()

    def __gt__(self, other):
        return self.__add__() > other.__add__()

    def __str__(self):
        return 'Name: {}\nCAO: {}\nPoints: {}'.format(self.name, self.cao, self.__add__())
