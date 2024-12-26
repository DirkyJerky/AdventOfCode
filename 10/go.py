from operator import ifloordiv
from pathlib import Path
import numpy as np
import networkx as nx

def parse_grid():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    return np.asarray(list(map(lambda st: list(st.strip()), input)), dtype=int)

grid = parse_grid()

graph = nx.DiGraph()

for (x,y), val in np.ndenumerate(grid):
    adjacents = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]

    for (x_adj, y_adj) in adjacents:
        if 0 <= x_adj < grid.shape[0] and 0 <= y_adj < grid.shape[1]:
            val_adj = grid[(x_adj, y_adj)]

            if val + 1 == val_adj:
                graph.add_edge((x,y,val),(x_adj, y_adj, val_adj))

froms = []
tos = []
for node in graph.nodes():
    (_, _, val) = node
    if (val == 0):
        froms.append(node)
    elif val == 9:
        tos.append(node)

num_paths = 0

for from_node in froms:
    for to_node in tos:
        if nx.has_path(graph, from_node, to_node):
            num_paths += 1

print('10a', num_paths)

num_distinct_paths = 0

for from_node in froms:
    for to_node in tos:
        if nx.has_path(graph, from_node, to_node):
            for p in nx.all_shortest_paths(graph, source=from_node, target=to_node):
                num_distinct_paths += 1

print('10b', num_distinct_paths)
