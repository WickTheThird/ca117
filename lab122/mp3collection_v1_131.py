#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration=0):
        self.title = title
        self.duration = duration

    def __str__(self):
        return 'Title: {}\nDuration: {}'.format(
            self.title, self.duration
        )

class MP3Collection(object):

    def __init__(self):
        self.agenda = {}

    def add(self, other):
        self.agenda[other.title] = other.duration

    def lookup(self, other):
        if other in self.agenda:
            return MP3Track(other, self.agenda[other])

    def remove(self, title):
        if title in self.agenda:
            del self.agenda[title]
