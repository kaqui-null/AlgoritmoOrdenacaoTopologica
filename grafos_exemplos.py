import matplotlib.pyplot as plt
import networkx as nx


def plot_graph(edges, label, highlight_cycle=False):
    G = nx.DiGraph()
    G.add_edges_from(edges)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(6, 4))
    manager = plt.get_current_fig_manager()
    manager.window.wm_title(label)

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


def exemplo1():
    edges = [(1, 2), (2, 3), (3, 4)]
    plot_graph(edges, "Exemplo 1 – Grafo em linha")


def exemplo2():
    edges = [(1, 3), (2, 3), (3, 4)]
    plot_graph(edges, "Exemplo 2 – Múltiplas raízes")


def exemplo3():
    edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
    plot_graph(edges, "Exemplo 3 – Ramificações")


def exemplo4():
    edges = [(5, 0), (5, 2), (4, 0), (4, 1), (2, 3), (3, 1)]
    plot_graph(edges, "Exemplo 4 – DAG com profundidade")


def exemplo5():
    edges = [(1, 2), (2, 3), (4, 5)]
    plot_graph(edges, "Exemplo 5 – Grafo desconexo")


def exemplo6():
    edges = [(1, 5), (2, 5), (3, 5), (4, 5)]
    plot_graph(edges, "Exemplo 6 – Vários indo para 1 destino")


def exemplo7():
    edges = [(1, 2), (2, 3), (3, 1)]
    plot_graph(edges, "Exemplo 7 – Grafo com ciclo", highlight_cycle=True)


def main():
    exemplo1()
    exemplo2()
    exemplo3()
    exemplo4()
    exemplo5()
    exemplo6()
    exemplo7()


if __name__ == "__main__":
    main()