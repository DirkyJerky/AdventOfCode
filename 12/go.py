from pathlib import Path
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def parse_grid():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    return np.asarray(list(map(lambda st: list(st.strip()), input)), dtype=str)

grid = parse_grid()

graph = nx.Graph()

for (x,y), val in np.ndenumerate(grid):
    adjacents = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]

    graph.add_node((x,y))

    for (x_adj, y_adj) in adjacents:
        if 0 <= x_adj < grid.shape[0] and 0 <= y_adj < grid.shape[1]:
            val_adj = grid[(x_adj, y_adj)]

            if val == val_adj:
                graph.add_edge((x,y),(x_adj, y_adj))

price_a = 0
price_b = 0

for c in nx.connected_components(graph):
    subgraph = graph.subgraph(c)

    N = len(subgraph.nodes)
    E = len(subgraph.edges)

    price_a += N * (4*N - 2*E)

    edge_set = nx.Graph()

    for (x,y) in subgraph.nodes:
        # up
        if (x, y-1) not in subgraph.nodes:
            edge_set.add_edge((x,y),(x+1,y))
        # right
        if (x+1, y) not in subgraph.nodes:
            edge_set.add_edge((x+1,y),(x+1,y+1))
        # down
        if (x, y+1) not in subgraph.nodes:
            edge_set.add_edge((x+1,y+1),(x,y+1))
        # left
        if (x-1, y) not in subgraph.nodes:
            edge_set.add_edge((x,y+1),(x,y))

    num_sides = 0
    # nx.draw(edge_set, with_labels=True)
    # plt.show()

    for cycle_graph_components in nx.simple_cycles(edge_set):
        # print(cycle_graph_components)
        cycle_graph = edge_set.subgraph(cycle_graph_components)
        # print(cycle_graph)
        # nx.draw(cycle_graph, with_labels=True)
        # plt.show()
        cycle = list(nx.find_cycle(cycle_graph))

        edge_offsets = []
        # print('new')
        for edge in cycle:
            ((x1,y1), (x2,y2)) = edge
            # print(x1,y1)
            edge_offsets.append((x2-x1, y2-y1))

        first_offset = edge_offsets[0]
        while edge_offsets[0] == first_offset:
            edge_offsets = edge_offsets[1:]
            edge_offsets.append(first_offset)

        curr_side_length = 0
        curr_side_offset = edge_offsets[0]

        for offset in edge_offsets:
            if offset == curr_side_offset:
                curr_side_length += 1
            else:
                num_sides += 1
                curr_side_length = 1
                curr_side_offset = offset
        num_sides += 1

        # print(side_lengths)

    price_b += num_sides * len(subgraph.nodes)


print('12a', price_a)
print('12b', price_b)
