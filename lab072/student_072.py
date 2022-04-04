#!/usr/bin/env python3

class Student(object):

    def __init__(self, sid, name, modlist=None):
        self.sid = sid
        self.name = name
        self.modlist = [] if modlist is None else modlist

    def add_module(self, new_mod):
        self.modlist.append(new_mod)

    def del_module(self, old_mod):
        find = self.modlist.index(old_mod)
        self.modlist.pop(find)

    def __str__(self):
        return 'ID: {}\nName: {}\nModules: {}'.format(
            self.sid, self.name, ", ".join(self.modlist)
        )
