#!/usr/bin/env python3

class Point(object):

    def set_attributes(self, x, y):
        self.x = x
        self.y = y

    def print_attributes(self):
        print('x:', f'{self.x:.2f}')
        print('y:', f'{self.y:.2f}')

    def reflect(self):
        inv_x = (-1) * int(self.x)
        inv_y = (-1) * int(self.y)
        self.x = inv_x
        self.y = inv_y
