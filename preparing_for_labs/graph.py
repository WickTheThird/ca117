import sys

points = sys.stdin.readlines()

class Graph(object):

    def __init__(self, roads):
        self.roads = roads
        self.paths = {}
        self.visited = []
        self.final_path = []

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
            if len(self.paths[point]) > 1 and point:
                self.final_path.append(point)
            for x in self.paths[point]:
                    self.has_path_to(x, final)
        elif point == final:
            self.visited.append(final)

    def has_path_to(self, init, final):
        if init in self.paths and init not in self.visited and init != final:
            self.visited.append(init)
            if self.visited[0] not in self.final_path:
                self.final_path.append(self.visited[0])
            for x in self.paths[init]:
                self.go_to_key(x, init, final)
        elif init == final:
            self.final_path.append(final)
            print(self.final_path)


f = points[0]
points = points[1:]

g = Graph(f)

for x in points:
    x = x.strip().split()
    g.add_path(int(x[0]), int(x[1]))

g.has_path_to(0, 6)
