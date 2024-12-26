from pathlib import Path
from networkx.exception import NetworkXNoPath
import numpy as np
import networkx as nx

def parse():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    return list(map(lambda l: l.split(','), input))


size = 70

grid = parse()

graph = nx.DiGraph()

for x in range(size+1):
    for y in range(size+1):
        for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0)]:
            tx = x+dx
            ty = y+dy

            if 0 <= tx <= size and 0 <= ty <= size:
                graph.add_edge((x,y),(tx,ty))

n = 1024

for i in range(n):
    (sx, sy) = grid[i]

    graph.remove_node((int(sx), int(sy)))

print('18a', nx.shortest_path_length(graph, (0,0), (size,size)))

for i in range(1024,len(grid)):
    (sx, sy) = grid[i]

    graph.remove_node((int(sx), int(sy)))
    try:
        nx.shortest_path_length(graph, (0,0), (size,size))
    except NetworkXNoPath:
        print('18b', (sx,sy))
        break
