from pathlib import Path
import numpy as np
import networkx as nx

def parse_grid():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    empty = input.index('\n')

    return (
        np.asarray(list(map(lambda st: list(st.strip()), input[:empty]))),
        "".join(list(map(lambda st: st.strip(), input[empty:])))
    )

(grid, instructions) = parse_grid()

# (dy,dx)
direction_map = {
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
}

robot = np.where(grid == '@')
robot = (int(robot[0][0]), int(robot[1][0]))
print(robot)

def attempt_move(at: tuple[int, int], delta: tuple[int, int]) -> bool:
    # print('attempt', at,delta)
    if grid[at] == '.':
        return True
    elif grid[at] == '#':
        return False
    elif grid[at] == '@' or grid[at] == 'O':
        (x,y) = at
        (dx,dy) = delta
        to = (x+dx, y+dy)
        if attempt_move(to, delta):
            grid[to] = grid[at]
            grid[at] = '.'
            return True
        else:
            return False
    else:
        return False

for chr in instructions:
    # print(grid)
    # print(chr)
    if attempt_move(robot, direction_map[chr]):
        (x,y) = robot
        (dx,dy) = direction_map[chr]
        robot = (x+dx, y+dy)

(boxes_x, boxes_y) = np.where(grid == 'O')
print('15a', sum(100*boxes_x) + sum(boxes_y))

print(grid)

(grid, instructions) = parse_grid()

np.set_printoptions(threshold=10000)
grid2 = np.full((grid.shape[0], grid.shape[1] * 2), '.')
for (y,x), item in np.ndenumerate(grid):
    if item == '@':
        grid2[(y, x*2)] = '@'
    elif item == 'O':
        grid2[(y,x*2)] = '['
        grid2[(y,x*2+1)] = ']'
    elif item == '#':
        grid2[(y,x*2)] = '#'
        grid2[(y,x*2+1)] = '#'

grid = grid2
# print(grid)


robot = np.where(grid == '@')
robot = (int(robot[0][0]), int(robot[1][0]))
print(robot)

def attempt_move_v2(
    at: tuple[int, int],
    delta: tuple[int, int],
    dry_run: bool
) -> bool:
    # print('attempt', at, delta, dry_run)
    # print('attempt', at,delta)
    if grid[at] == '.':
        return True
    elif grid[at] == '#':
        return False
    elif grid[at] == '@':
        (y,x) = at
        (dy,dx) = delta
        to = (y+dy,x+dx)
        if attempt_move_v2(to, delta, True):
            attempt_move_v2(to, delta, False)
            grid[to] = grid[at]
            grid[at] = '.'
            return True
        else:
            return False
    elif grid[at] == '[' or grid[at] == ']':
        (y,x) = at
        (dy,dx) = delta
        to = (y+dy,x+dx)
        if delta[1] == 0:
            partner = (y, x + (1 if grid[at] == '[' else -1))
            partner_to = (partner[0]+dy, partner[1]+dx)
            if attempt_move_v2(to, delta, dry_run) and attempt_move_v2(partner_to, delta, dry_run):
                if not dry_run:
                    grid[to] = grid[at]
                    grid[at] = '.'
                    grid[partner_to] = grid[partner]
                    grid[partner] = '.'
                return True
            else:
                return False
        else:
            if attempt_move_v2(to, delta, True):
                attempt_move_v2(to, delta, False)
                grid[to] = grid[at]
                grid[at] = '.'
                return True
            else:
                return False
    else:
        return False

for chr in instructions:
    # for line in grid:
    #     print("".join(line))
    # print(chr)
    if attempt_move_v2(robot, direction_map[chr], True):
        (x,y) = robot
        (dx,dy) = direction_map[chr]
        robot = (x+dx, y+dy)

# print(grid)
for line in grid:
        print("".join(line))

(boxes_x, boxes_y) = np.where(grid == '[')
print('15b', sum(100*boxes_x) + sum(boxes_y))
