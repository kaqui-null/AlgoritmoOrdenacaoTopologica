from collections import deque
import matplotlib.pyplot as plt
import networkx as nx
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

    def is_cyclic(self) -> bool: # algoritmo de Khan

        in_degree = {}
        for v in self.vertices.values():
            in_degree[v.id] = 0

        for v in self.vertices.values():
            for neighbor in v.neighbors:
                if neighbor.id in in_degree:
                    in_degree[neighbor.id] += 1
                else:
                    in_degree[neighbor.id] = 1

        queue = deque([v_id for v_id in in_degree if in_degree[v_id] == 0])
        visited = 0

        while queue:
            current = queue.popleft()
            visited += 1

            for neighbor in self.vertices[current].neighbors:
                in_degree[neighbor.id] -= 1
                if in_degree[neighbor.id] == 0:
                    queue.append(neighbor.id)

        return visited != len(self.vertices)

class TopologicalSort:
    def __init__(self):
        pass

    def sort(self, graph) -> list:
        if graph.is_cyclic():
            return []
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

class Plotting:
    def plot_graph(self, edges, label, highlight_cycle=False):
        G = nx.DiGraph()
        G.add_edges_from(edges)

        pos = nx.spring_layout(G, seed=42)

        plt.figure(figsize=(6, 4))

        nx.draw(
            G, pos,
            with_labels=True,
            node_color='skyblue',
            node_size=1200,
            edge_color='gray',
            arrowsize=20,
            font_weight='bold'
        )

        if highlight_cycle:
            try:
                cycle = nx.find_cycle(G, orientation='original')
                cycle_edges = [(u, v) for u, v, _ in cycle]
                nx.draw_networkx_edges(G, pos, edgelist=cycle_edges, edge_color='red', width=3)
            except nx.NetworkXNoCycle:
                print("Não foi encontrado ciclo, mesmo com highlight_cycle=True")

        plt.text(
            0.5, 1.05, label,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=14,
            fontweight='bold',
            transform=plt.gca().transAxes
        )

        plt.axis('off')
        plt.subplots_adjust(top=0.85)
        plt.show()


    def exemplo1(self):
        edges = [(1, 2), (2, 3), (3, 4)]

        g = Graph()
        for edge in edges:
            g.new_edge(edge[0], edge[1])

        tSort = TopologicalSort()
        print(tSort.sort(g))

        self.plot_graph(edges, "Exemplo 1 – Grafo em linha")


    def exemplo2(self):
        edges = [(1, 3), (2, 3), (3, 4)]
        g = Graph()
        for edge in edges:
            g.new_edge(edge[0], edge[1])

        tSort = TopologicalSort()
        print(tSort.sort(g))

        self.plot_graph(edges, "Exemplo 2 – Múltiplas raízes")


    def exemplo3(self):
        edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
        g = Graph()
        for edge in edges:
            g.new_edge(edge[0], edge[1])

        tSort = TopologicalSort()
        print(tSort.sort(g))

        self.plot_graph(edges, "Exemplo 3 – Ramificações")


    def exemplo4(self):
        edges = [(5, 0), (5, 2), (4, 0), (4, 1), (2, 3), (3, 1)]
        g = Graph()
        for edge in edges:
            g.new_edge(edge[0], edge[1])

        tSort = TopologicalSort()
        print(tSort.sort(g))

        self.plot_graph(edges, "Exemplo 4 – DAG com profundidade")


    def exemplo5(self):
        edges = [(1, 2), (2, 3), (4, 5)]
        g = Graph()
        for edge in edges:
            g.new_edge(edge[0], edge[1])

        tSort = TopologicalSort()
        print(tSort.sort(g))

        self.plot_graph(edges, "Exemplo 5 – Grafo desconexo")


    def exemplo6(self):
        edges = [(1, 5), (2, 5), (3, 5), (4, 5)]
        g = Graph()
        for edge in edges:
            g.new_edge(edge[0], edge[1])

        tSort = TopologicalSort()
        print(tSort.sort(g))

        self.plot_graph(edges, "Exemplo 6 – Vários indo para 1 destino")


    def exemplo7(self):
        edges = [(1, 2), (2, 3), (3, 1)]
        g = Graph()
        for edge in edges:
            g.new_edge(edge[0], edge[1])

        tSort = TopologicalSort()
        print(tSort.sort(g))

        self.plot_graph(edges, "Exemplo 7 – Grafo com ciclo", highlight_cycle=True)


def main():
    plt = Plotting()
    plt.exemplo1()
    plt.exemplo2()
    plt.exemplo3()
    plt.exemplo4()
    plt.exemplo5()
    plt.exemplo6()
    plt.exemplo7()


if __name__=="__main__":
    main()
