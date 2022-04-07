#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao

    def __str__(self):
        return 'Name: {}\nCAO: {}'.format(self.name, self.cao)

class Classlist(object):

    def __init__(self):
        self.log = {}

    def add(self, student):
        self.log[student.cao] = student.name

    def lookup(self, cao):
        if cao in self.log:
            return Student(self.log[cao], cao)
        return None

    def remove(self, cao):
        if cao in self.log:
            del self.log[cao]
