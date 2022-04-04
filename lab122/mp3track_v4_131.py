#!/usr/bin/env python3

import datetime

class MP3Track(object):

    def __init__(self, title, duration, artists=[]):
        self.title = title
        self.duration = duration
        self.artists = artists

    def add_artist(self, artist):
        self.artists.append(artist)

    def convert(self, time):
        if str(datetime.timedelta(seconds=time))[2:4] == '00':
            m = str(datetime.timedelta(seconds=time))[3:]
            return m
        elif int(str(datetime.timedelta(seconds=time))[3]) == 0:
            m = str(datetime.timedelta(seconds=time))[2:]
            return m
        elif int(str(datetime.timedelta(seconds=time))[3:4]) > 0:
            m = str(datetime.timedelta(seconds=time))[3:]
            return m
        elif int(str(datetime.timedelta(seconds=time))[:1]) > 0:
            m = str(datetime.timedelta(seconds=time))
            return m

    def __str__(self):
        return 'Title: {}\nBy: {}\nDuration: {}'.format(
            self.title, ', '.join(self.artists).strip(), self.convert(self.duration)
        )
