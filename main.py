
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
        self.new_vertice(destiny)
        self.vertices[origin].new_neighbor(self.vertices[destiny])

class TopologicalSort:
    def __init__(self):
        pass

    def sort(self, graph) -> list:
        visited = set()
        stack = []
        vertices = graph.vertices

        for vertice in vertices.values():
            if vertice not in visited:
                self.dfs(vertice, visited, stack)
        
        return [v.id for v in stack]

    def dfs(self, vertice, visited, stack) -> int:
        visited.add(vertice)
        for neighbor in vertice.neighbors:
            if neighbor not in visited:
                self.dfs(neighbor, visited, stack)
        
        stack.insert(0, vertice)

def main():
    exemplo_grafo1()

def exemplo_grafo1():
    g = Graph()
    g.new_edge(7, 11)
    g.new_edge(7, 8)
    g.new_edge(5, 11)
    g.new_edge(3, 8)
    g.new_edge(3, 10)
    g.new_edge(11, 2)
    g.new_edge(11, 9)
    g.new_edge(11, 10)
    g.new_edge(8, 9)

    tSort = TopologicalSort()

    print(g.vertices)
    print(tSort.sort(graph=g))

if __name__=="__main__":
    main()
