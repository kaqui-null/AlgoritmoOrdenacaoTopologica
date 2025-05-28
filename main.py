
class Vertice:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def new_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

class Graph:
    def __init__(self):
        self.vertices = {}

    def new_vertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)

    def new_edge(self, origin, destiny):
        self.new_vertice(origin)
        self.new_neighbor(destiny)
        self.vertices[origin].new_neighbor(self.vertices[destiny])

class TopologicalSort:
    def sort() -> list:
        pass

    def dfs() -> Vertice:
        pass

class Main:
    def main():
        pass

if __name__=="__main__":
    Main.main()
