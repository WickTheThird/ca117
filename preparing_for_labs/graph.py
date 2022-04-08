import sys

points = sys.stdin.readlines()

class Graph(object):

    def __init__(self, roads):
        self.paths = {}
        self.visited = []

    def add_path(self, init, final):
        if init not in self.paths:
            self.paths[init] = [final]
        elif init in self.paths:
            self.paths[init].append(final)
        if final not in self.paths:
            self.paths[final] = [init]
        elif final in self.paths:
            self.paths[final].append(init)

    def go_to_key(self, point, init, final):
        if point in self.paths and point not in self.visited and point != final:
            self.visited.append(point)
            for x in self.paths[point]:
                    self.has_path_to(x, final)
        elif point == final:
            if final not in self.visited:
                self.visited.append(final)
                return self.visited

    def has_path_to(self, init, final):
        self.final = final
        if init in self.paths and init not in self.visited and init != final:
            self.visited.append(init)
            for x in self.paths[init]:
                self.go_to_key(x, init, final)
        elif init == final:
            if final not in self.visited:
                self.visited.append(final)
                return self.visited

    def print_path(self):
        for i, x in enumerate(self.visited):
            if i + 1 < len(self.visited) and x != self.final:
                if x not in self.paths[self.visited[i + 1]]:
                    self.visited.pop(i)
                    if self.visited[i] == self.final:
                        self.visited = self.visited[:i + 1]
                        break
            if x == self.final:
                self.visited = self.visited[:i + 1]
        print(self.visited)


f = points[0]
points = points[1:]

g = Graph(f)

for x in points:
    x = x.strip().split()
    g.add_path(int(x[0]), int(x[1]))

g.has_path_to(2, 1)
g.print_path()
