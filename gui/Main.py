import networkx as nx
import matplotlib.pyplot as plt
from numpy import random, array
import random as rd


def main():
    graph, colors = gen_random_graph(100)
    show_default_graph(graph, colors)


def random_basic_graph(size):
    """
    Returns a random graph with `size` nodes.
    Each node have the same color.
    """
    graphs = [nx.DiGraph()]

    default_ord = [i for i in range(size)]
    default_arr = array(default_ord)
    permutation = random.permutation(default_arr)

    graphs[-1].add_edges_from([(i, permutation[i]) for i in range(size)])
    nx.draw_circular(graphs[-1], with_labels=True)
    return graphs, []


def gen_random_graph(size):
    """
    Returns a list of random graph of `size` nodes.
    Connected components are separated into multiple subgraphs.
    Each subgraph have a different color.
    """
    default_ord = [i for i in range(size)]
    default_arr = array(default_ord)
    permutation = random.permutation(default_arr)

    return __sorted_edges([], size, default_ord, permutation)


def random_color(limit):
    """
    Returns a random color with `0.7` transparency.
    Text can be write in black on those colors.
    """
    colortuple = tuple([rd.random() for _ in range(3)] + [0.7])
    (red, green, blue, _) = colortuple

    while (red * 0.299 + green * 0.587 + blue * 0.114) > 186:
        colortuple = tuple([rd.random() for _ in range(3)] + [0.7])
        (red, green, blue, _) = colortuple

    return colortuple


def __sorted_edges(graphs, size, default_ord, permutation):
    """
    Based on a permutation, define link between nodes.
    """
    current = 0
    colors = [[]]
    current_color = random_color(size)
    graphs.append(nx.DiGraph())

    for _ in range(size):
        colors[-1].append(current_color)
        next = permutation[current]

        if current != next:
            graphs[-1].add_edge(current, next)
        else:
            graphs[-1].add_node(current)
            graphs.append(nx.DiGraph())
            colors += [[]]
            current_color = random_color(size)

        default_ord.remove(current)

        if len(default_ord) == 0:
            break

        if next in default_ord:
            current = next
        else:
            current = default_ord[0]
            colors += [[]]
            current_color = random_color(size)
            graphs.append(nx.DiGraph())

    return graphs, colors


def show_default_graph(graphs, colors):
    cycles = len(graphs)

    centers = nx.Graph()
    for i in range(cycles):
        centers.add_node(i)

    centered_pos = nx.spring_layout(centers)

    for graph, color, center in zip(graphs, colors, centered_pos.values()):
        scale = 0.01 * len(color)
        pos = nx.shell_layout(graph, scale=scale, center=center)
        nx.draw(graph, pos, node_color=color, with_labels=True)
        nx.draw_networkx_labels(graph, pos, font_size=12, font_color="black")
    plt.show()


if __name__ == "__main__":
    main()
