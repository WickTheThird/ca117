import sys

listing = sys.stdin.readlines()

class Vertical(object):

    def __init__(self):
        self.ageda = {}

    def flip_order(self, list_1):
        for x in list_1:
            self.assign_letter(x.strip())

    def assign_letter(self, word):
        for count, x in enumerate(word):
            if count not in self.ageda:
                self.ageda[count] = x
            elif count in self.ageda:
                self.ageda[count] = self.ageda[count] + x

    def sort(self):
        return sorted(self.ageda.values(), key=str.lower)

    def __str__(self):
        total = ''
        for x in self.ageda.values():
            total = total + x + '\n'
        return total.strip()


m = Vertical()
n = Vertical()
m.flip_order(listing)
n.flip_order(m.sort())
print(n)
