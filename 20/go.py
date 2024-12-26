from pathlib import Path
import numpy as np
import networkx as nx

def parse_grid():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    return np.asarray(list(map(lambda st: list(st.strip()), input)))

adj_list = [
    (0, -1),
    (-1, 0),
    (1, 0),
    (0, 1)
]

grid = parse_grid()

graph = nx.DiGraph()

start = np.where(grid == 'S')
start = (int(start[0][0]), int(start[1][0]))

end = np.where(grid == 'E')
end = (int(end[0][0]), int(end[1][0]))

for (y,x), chr in np.ndenumerate(grid):
    if chr == '#':
        continue

    for (dy,dx) in adj_list:
        adj = (y+dy, x+dx)
        if grid[adj] != '#':
            graph.add_edge((y,x), (adj[0],adj[1]))

path = nx.shortest_path(graph, start, end)

len_dict: dict[tuple[int, int], int] = {}

for i, node in enumerate(path):
    len_dict[node] = i

lens = []

for (y,x), chr in np.ndenumerate(grid):
    if chr != '#':
        continue

    if y == 0 or x == 0:
        continue

    if y == grid.shape[0]-1 or x == grid.shape[1]-1:
        continue

    for (dy,dx) in adj_list:
        for (dy2, dx2) in adj_list:
            if (dy == dy2) and (dx == dx2):
                continue

            adj1 = (y+dy, x+dx)
            adj2 = (y+dy2, x+dx2)
            if grid[adj1] != '#' and grid[adj2] != '#':
                diff_savings = len_dict[adj1] - len_dict[adj2] - 2
                if 0 < diff_savings:
                    lens.append(diff_savings)

print('20a', len(list(filter(lambda x: x >= 100, lens))))

lens = []

for (y,x), chr in np.ndenumerate(grid):
    if chr == '#':
        continue

    for dy in range(-20, 21):
        max_x = 20 - abs(dy)
        for dx in range(-max_x, max_x+1):
            end_pos = (y+dy,x+dx)

            if end_pos[0] < 0 or end_pos[0] >= grid.shape[0]:
                continue
            if end_pos[1] < 0 or end_pos[1] >= grid.shape[1]:
                continue
            if grid[end_pos] == '#':
                continue

            cheat_len = abs(dy)+abs(dx)

            diff = len_dict[end_pos] - len_dict[(y,x)]

            savings = diff - cheat_len

            if savings > 0:
                lens.append(savings)

print('20b', len(list(filter(lambda x: x >= 100, lens))))
