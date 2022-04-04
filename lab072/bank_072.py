#!/usr/bin/env python3

class BankAccount(object):

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, dep):
        self.balance = self.balance + dep

    def withdraw(self, wid):
        if self.balance >= wid:
            self.balance = self.balance - wid

    def __str__(self):
        return 'Your current balance is {:.2f} euro'.format(
            self.balance
        )
