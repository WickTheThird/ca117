#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao
        self.log = {}
        self.popular = {}

    def add_grade(self, mod, grade):
        self.log[mod] = grade
        if mod not in self.popular:
            self.popular[mod] = 1
        elif mod in self.popular:
            self.popular[mod] = self.popular[mod] + 1

    def get_grade(self, mod):
        if mod in self.log:
            return self.log[mod]
        return 'N/A'

    def __str__(self):
        return 'Name: {}\nCAO: {}'.format(
            self.name, self.cao)

class Classlist(object):

    def __init__(self):
        self.agenda = {}
        self.popular = {}

    def add(self, other):
        self.agenda[other.cao] = other.name
        for x in other.popular:
            if x not in self.popular:
                self.popular[x] = other.popular[x]
            elif x in self.popular:
                self.popular[x] = self.popular[x] + 1

    def remove(self, cao):
        if cao in self.agenda:
            del self.agenda[cao]

    def lookup(self, cao):
        for x in self.agenda:
            if x == cao:
                return Student(self.agenda[x], x)
        return None

    def most_popular_subject(self):
        m = max(self.popular.values())
        for x in self.popular:
            if self.popular[x] == m:
                return x
        return None

    def __str__(self):
        final = []
        for x in sorted(self.agenda):
            this = 'Name: {}\nCAO: {}'.format(self.agenda[x], x)
            final.append(this)
        return '\n'.join(final)
