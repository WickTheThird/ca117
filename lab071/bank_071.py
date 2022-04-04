#!/usr/bin/env python3

class BankAccount(object):

    def set_attributes(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def print_attributes(self):
        print('Name:', self.name)
        print('Account number:', self.number)
        print('Balance:', f'{self.balance:.2f}')

    def deposit(self, increase):
        m = self.balance
        total = m + increase
        self.balance = total
