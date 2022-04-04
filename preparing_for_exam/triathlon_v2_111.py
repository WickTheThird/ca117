#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return 'Name: {}\nID: {}'.format(
            self.name, self.tid
        )

class Triathlon(object):

    def __init__(self):
        self.agenda = {}

    def add(self, other):
        self.agenda[other.tid] = other.name

    def remove(self, tid):
        del self.agenda[tid]

    def lookup(self, tid):
        for x in self.agenda:
            if x == tid:
                return Triathlete(self.agenda[x], tid)
        return None

    def __str__(self):
        dict = {value: key for key, value in self.agenda.items()}
        sorting_dict = sorted(dict)
        total = ''
        for x in sorting_dict:
            total = total + 'Name: {}\nID: {}\n'.format(
                x, str(dict[x])
            )
        return total.strip()
