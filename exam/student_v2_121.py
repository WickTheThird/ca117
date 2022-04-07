#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.agenda = {}
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

    def __str__(self):
        return 'Name: {}\nCAO: {}'.format(self.name, self.cao)
