from pathlib import Path
from typing import Generator
import numpy as np
import networkx as nx
from numpy._typing import NDArray
from functools import cache

def parse():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    sep = input.index('\n')

    def parse_init_line(l: str):
        key, val = l.split(':')
        return (key.strip(), val.strip() == '1')

    initials = list(map(parse_init_line, input[:sep]))

    def parse_gates_line(l: str):
        parts = l.split()
        return (parts[1], parts[0], parts[2], parts[4])

    gates = list(map(parse_gates_line, input[sep+1:]))

    return (initials, gates)

graph = nx.DiGraph()

inits, gates = parse()

for key, val in inits:
    graph.add_node(key)
    graph.nodes[key]['val'] = val

for op, in1, in2, out in gates:
    graph.add_edge(in1, out)
    graph.add_edge(in2, out)
    graph.nodes[out]['op'] = op
    graph.nodes[out]['val'] = None

def get_val(node: str) -> bool:
    assert node in graph.nodes

    if graph.nodes[node]['val'] is not None:
        return graph.nodes[node]['val']

    in_edges = graph.in_edges(node)

    in_edges = list(graph.in_edges(node))

    val1 = get_val(in_edges[0][0])
    val2 = get_val(in_edges[1][0])

    op = graph.nodes[node]['op']

    out = None
    if op == 'AND':
        out = val1 and val2
    elif op == 'OR':
        out = val1 or val2
    elif op == 'XOR':
        out = val1 ^ val2

    assert out is not None

    graph.nodes[node]['val'] = out

    # print('calc', node, val1, op, val2, '=', out)

    return out

i: int = 0
num = 0

while True:
    node = f'z{i:02}'

    if node not in graph.nodes:
        break

    if get_val(node):
        num += (2**i)

    i += 1

print('24a', num)
