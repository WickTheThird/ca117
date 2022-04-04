#!/usr/bin/env python3

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

    def add(self, other):
        self.agenda[other] = other.artists

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
