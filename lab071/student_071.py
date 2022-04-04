#!/usr/bin/env python3

class Student(object):

    def set_attributes(self, sid, name, modlist):
        self.sid = sid
        self.name = name
        self.modlist = modlist

    def print_attributes(self):
        print('ID:', self.sid)
        print('Name:', self.name)
        print('Modules:', ", ".join(self.modlist).strip())

    def add_module(self, new_mod):
        self.modlist.append(new_mod)

    def del_module(self, del_mod):
        position = self.modlist.index(del_mod)
        self.modlist.pop(position)
