#!/usr/bin/env python3

class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return '{} {} {}'.format(
            self.name, self.phone, self.email
        )

class ContactList(object):

    def __init__(self):
        self.mydict = {}

    def add(self, contact):
        self.mydict[contact.name] = contact

    def remove(self, name):
        if name in self.mydict:
            del self.mydict[name]

    def get(self, name):
        if name in self.mydict:
            return self.mydict[name]
        return None

    def __str__(self):
        list = sorted([str(x) for x in self.mydict.values()])
        return 'Contact list\n------------\n{}'.format(
            '\n'.join(list)
        )
