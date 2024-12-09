from pathlib import Path
from multiset import Multiset
import re
import networkx as nx

with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
    input = input_file.readlines()

starting_cursor = (0,0,'^')
cursor = (0,0,'^')

# cell = (is_obstacle, is_visited)

height = len(input)
width = len(input[0])

grid: list[list[tuple[bool, bool]]] = [[(False, False) for x in range(width)] for y in range(height)]

for y, line in enumerate(input):
    for x, chr in enumerate(line):
        if chr == '^':
            cursor = (x,y,'^')
            starting_cursor = (x,y,'^')

            grid[y][x] = (False, True)
        elif chr == '#':
            grid[y][x] = (True, False)
        else:
            grid[y][x] = (False, False)


direction_map = {
    '^': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1)
}

evolution_map = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

while True:
    (x, y, dir) = cursor
    (x_off, y_off) = direction_map[dir]

    next_x = x + x_off
    next_y = y + y_off

    if (
        next_x < 0
        or next_y < 0
        or next_y >= len(grid)
        or next_x >= len(grid[0])
    ):
        break

    (is_obstacle, _) = grid[next_y][next_x]

    if is_obstacle:
        cursor = (x, y, evolution_map[dir])
    else:
        grid[next_y][next_x] = (is_obstacle, True)
        cursor = (next_x, next_y, dir)

num_visited = 0

for y, row in enumerate(grid):
    for x, (_, visited) in enumerate(row):
        if visited:
            num_visited += 1

print('6a', num_visited)

(starting_x, starting_y, __) = starting_cursor

found_loops = 0

for potential_obstacle_x in range(width):
    for potential_obstacle_y in range(height):
        if grid[potential_obstacle_y][potential_obstacle_x][0] == True:
            continue
        if potential_obstacle_x == starting_x and potential_obstacle_y == starting_y:
            continue

        grid[potential_obstacle_y][potential_obstacle_x] = (True, False)
        cursor = (starting_x, starting_y, '^')

        past_cursors = set()

        while True:
            if cursor in past_cursors:
                # print('loop at', potential_obstacle_x, potential_obstacle_y)
                # print(found_loops)
                found_loops += 1
                break
            else:
                past_cursors.add(cursor)

            (x, y, dir) = cursor
            (x_off, y_off) = direction_map[dir]

            next_x = x + x_off
            next_y = y + y_off

            if (
                next_x < 0
                or next_y < 0
                or next_y >= len(grid)
                or next_x >= len(grid[0])
            ):
                break

            (is_obstacle, _) = grid[next_y][next_x]

            if is_obstacle:
                cursor = (x, y, evolution_map[dir])
            else:
                grid[next_y][next_x] = (is_obstacle, True)
                cursor = (next_x, next_y, dir)

        grid[potential_obstacle_y][potential_obstacle_x] = (False, False)

print('6b', found_loops)
