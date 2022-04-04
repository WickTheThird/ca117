#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.news = {}
        self.name = name
        self.tid = tid

    def add_time(self, event, time=0):
        self.news[event] = time

    def get_time(self, input):
        return self.news[input]

    def __add__(self):
        total = 0
        for x in self.news:
            total = total + self.news[x]
        return total

    def __eq__(self, other):
        return self.__add__() == other.__add__()

    def __lt__(self, other):
        return self.__add__() < other.__add__()

    def __gt__(self, other):
        return self.__add__() > other.__add__()

    def __str__(self):
        return 'Name: {}\nID: {}\nRace time: {}'.format(
            self.name, self.tid, self.__add__()
        )
