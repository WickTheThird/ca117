#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao
        self.log = {}

    def add_grade(self, mod, grade):
        self.log[mod] = grade

    def get_grade(self, mod):
        if mod in self.log:
            return self.log[mod]
        return 'N/A'

    def __str__(self):
        return 'Name: {}\nCAO: {}'.format(
            self.name, self.cao)
