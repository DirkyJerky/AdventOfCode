from pathlib import Path
import numpy as np
import networkx as nx

def parse_grid():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    return np.asarray(list(map(lambda st: list(st.strip()), input)))
# (dy,dx)
direction_map = {
    '<': (0, -1,'^'),
    '^': (-1, 0,'>'),
    'v': (1, 0,'<'),
    '>': (0, 1,'v'),
}

grid = parse_grid()

graph = nx.DiGraph()

start = np.where(grid == 'S')
start = (int(start[0][0]), int(start[1][0]),'>')

end = np.where(grid == 'E')
end1 = (int(end[0][0]), int(end[1][0]),'>')
end2 = (int(end[0][0]), int(end[1][0]),'^')

for (y,x), chr in np.ndenumerate(grid):
    if chr == '#':
        continue

    if chr == '.' or chr == 'S' or chr == 'E':
        for dir, (dy,dx,nxt) in direction_map.items():
            graph.add_edge((y,x,dir), (y,x,nxt), weight=1000)
            adj = (y+dy, x+dx)
            if grid[adj] == '.' or grid[adj] == 'E':
                graph.add_edge((y,x,dir), (adj[0],adj[1],dir), weight=1)

len1 = nx.dijkstra_path_length(graph, start, end1, 'weight')
len2 = nx.dijkstra_path_length(graph, start, end2, 'weight')

best = end1
if len2 < len1:
    best = end2

print('16a', min(len1,len2))

points_on_path = set()

for path in nx.all_shortest_paths(graph, start, best, 'weight'):
    # print('found path', path)
    for (y,x,_) in path:
        points_on_path.add((y,x))

print('16b', len(points_on_path))
