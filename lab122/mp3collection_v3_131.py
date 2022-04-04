#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration, artists):
        self.title = title
        self.duration = duration
        self.artists = artists

    def __str__(self):
        return 'Title: {}\nBy: {}\nDuration: {}'.format(
            self.title, ', '.join(self.artists).strip(), self.duration
        )

class MP3Collection(object):

    def __init__(self):
        self.agenda = {}
        self.agenda_2 = {}
        self.agenda_3 = {}

    def add(self, other):
        self.agenda[self] = other.title
        self.agenda_2[self] = other.duration
        self.agenda_3[self] = other.artists

    def lookup(self, other):
        if other in self.agenda:
            return MP3Track(other, self.agenda[other])

    def get_mp3s_by_artist(self, artist):
        log = []
        for x in self.agenda:
            if artist in self.agenda[x]:
                log.append(x)
        return log

    def remove(self, title):
        if title in self.agenda:
            del self.agenda[title]

    def __add__(self, other):
        new_duration = self.agenda_2[self] + other.agenda_2[other]
        new_title = self.agenda[self] + ' ' + other.agenda[other]
        new_artists = []
        for x in self.agenda.values():
            if x not in other.agenda.values():
                new_artists.append(x)
        self.add(MP3Track(new_title, new_duration, new_artists))
        return MP3Collection()

        print(self.agenda, other.agenda)
        print(self.agenda_2, other.agenda_2)
        print(self.agenda_3, other.agenda_3)
