#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao
        self.log = {}
        self.grades_s = []

    def add_grade(self, mod, grade):
        self.log[mod] = grade
        if grade in grades:
            self.grades_s.append(grades[grade])

    def get_grade(self, mod):
        if mod in self.log:
            return self.log[mod]
        return 'N/A'

    def __add__(self):
        total = 0
        self.grades_s = sorted(self.grades_s, reverse=True)
        for i, x in enumerate(self.grades_s):
            if i == 3:
                return total
            total = total + x
        return total

    def __lt__(self, other):
        return self.__add__() < other.__add__()

    def __gt__(self, other):
        return self.__add__() > other.__add__()

    def __eq__(self, other):
        return self.__add__() == other.__add__()

    def __str__(self):
        return 'Name: {}\nCAO: {}\nPoints: {}'.format(
            self.name, self.cao, self.__add__())


grades = {'H1': 100, 'H2': 88, 'H3': 77, 'H4': 66, 'H5': 56, 'H6': 46, 'H7': 37, 'H8': 0, 'O1': 56, 'O2': 46, 'O3': 37, 'O4': 28, 'O5': 20, 'O6': 12, 'O7': 0, 'O8': 0}
