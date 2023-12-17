import networkx as nx
import matplotlib.pyplot as plt
from numpy import random, array
import random as rd


def main():
    graph, colors = gen_random_graph(100)
    show_default_graph(graph, colors)


def gen_random_graph(size, distinct=True):
    G = nx.DiGraph()

    default_ord = [i for i in range(size)]
    default_arr = array(default_ord)
    permutation = random.permutation(default_arr)

    if distinct:
        return __sorted_edges(G, size, default_ord, permutation)

    G.add_edges_from([(i, permutation[i]) for i in range(size)])
    nx.draw_circular(graph, with_labels=True)
    return G, []


def random_color(limit):
    colortuple = tuple([rd.random() for _ in range(3)] + [0.7])
    (red, green, blue, _) = colortuple
    
    while (red*0.299 + green*0.587 + blue*0.114) > 186:
        colortuple = tuple([rd.random() for _ in range(3)] + [0.7])
        (red, green, blue, _) = colortuple

    return colortuple


def __sorted_edges(G, size, default_ord, permutation):
    current = 0
    colors = []
    current_color = random_color(size)
    for _ in range(size):
        colors.append(current_color)
        next = permutation[current]

        if current != next:
            G.add_edge(current, next)
        else:
            G.add_node(current)
            current_color = random_color(size)

        default_ord.remove(current)

        if len(default_ord) == 0:
            break

        if next in default_ord:
            current = next
        else:
            current = default_ord[0]
            current_color = random_color(size)

    return G, colors


def show_default_graph(graph, colors):
    pos = nx.circular_layout(graph);
    nx.draw(graph, pos, node_color=colors, with_labels=True)
    nx.draw_networkx_labels(graph, pos, font_size=12, font_color="black")
    plt.show()


if __name__ == "__main__":
    main()
