#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, hour=0, minute=0, duration=0):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return '{:02d}:{:02d} ({} minutes)'.format(
            self.hour, self.minute, self.duration
        )

class Schedule(object):

    def __init__(self):
        self.schedule = []

    def add(self, time):
        self.schedule.append(str(time))

    def __str__(self):
        return 'Schedule\n--------\n{}\nMeetings today: {}'.format(
            '\n'.join(sorted(self.schedule)), len(self.schedule)
        )
