from pathlib import Path
from typing import Generator
import numpy as np
import networkx as nx
from numpy._typing import NDArray
from functools import cache

def parse():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    return list(map(lambda l: l.strip().split('-'), input))

graph = nx.Graph()

for xs in parse():
    graph.add_edge(xs[0],xs[1])

num_ts = 0

# for cycle in nx.simple_cycles(graph, 3):
#     # print(cycle)
#     for node in cycle:
#         if node.startswith('t'):
#             num_ts += 1
#             break

# print('23a', num_ts)

max = []
for cliq in nx.find_cliques(graph):
    if len(cliq) > len(max):
        max = cliq

max.sort()

print('23b', ",".join(max))
