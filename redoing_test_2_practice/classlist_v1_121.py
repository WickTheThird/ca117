#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao

    def __str__(self):
        return 'Name: {}\nCAO: {}'.format(
            self.name, self.cao)

class Classlist(object):

    def __init__(self):
        self.agenda = {}

    def add(self, other):
        self.agenda[other.cao] = other.name

    def remove(self, cao):
        if cao in self.agenda:
            del self.agenda[cao]

    def lookup(self, cao):
        for x in self.agenda:
            if x == cao:
                return Student(self.agenda[x], x)
        return None
