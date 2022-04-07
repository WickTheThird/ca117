#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.agenda = {}
        self.popular = {}
        self.name = name
        self.cao = cao

    def add_grade(self, course, grade='N/A'):
        self.agenda[course] = grade
        if course not in self.popular:
            self.popular[course] = 1

    def get_grade(self, course):
        if course in self.agenda:
            for x in self.agenda:
                if x == course:
                        return self.agenda[course]
        else:
            return 'N/A'

    def __str__(self):
        return 'Name: {}\nCAO: {}'.format(self.name, self.cao)

class Classlist(object):

    def __init__(self):
        self.log = {}
        self.popular = {}
        self.score = {}

    def add(self, student):
        self.log[student.cao] = student.name
        self.popular[student] = student.popular

    def lookup(self, cao):
        if cao in self.log:
            return Student(self.log[cao], cao)
        return None

    def most_popular_subject(self):
        for x in self.popular:
            for y in self.popular[x]:
                if y not in self.score:
                    self.score[y] = 1
                elif y in self.score:
                    self.score[y] = self.score[y] + 1
        for x in self.score:
            if self.score[x] == max(self.score.values()):
                return x

    def remove(self, cao):
        if cao in self.log:
            del self.log[cao]
