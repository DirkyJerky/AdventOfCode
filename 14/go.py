from pathlib import Path
import numpy as np
import networkx as nx
import re
import math

from numpy.linalg import LinAlgError

def parse():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    regex = re.compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)')
    for line in input:
        yield regex.match(line).groups()

width = 11
height = 7

width = 101
height = 103

def iter_robot(robot):
    (x,y,dx,dy) = robot
    return ((x+dx) % width, (y+dy) % height, dx, dy)

robots_100 = []

for line in parse():
    (x,y,dx,dy) = line
    robot = (int(x),int(y),int(dx),int(dy))
    for _ in range(100):
        robot = iter_robot(robot)

    robots_100.append(robot)

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for (x,y,_,_) in robots_100:
    if x < width // 2:
        if y < height // 2:
            q1 += 1
        elif y > height // 2:
            q2 += 1
    elif x > width // 2:
        if y < height // 2:
            q3 += 1
        elif y > height // 2:
            q4 += 1

print('14a', q1*q2*q3*q4)

robots = []
iter = 0
next_stop = 8050

for line in parse():
    (x,y,dx,dy) = line
    robots.append((int(x),int(y),int(dx),int(dy)))

while True:
    if iter == next_stop:
        grid = [['.' for _ in range(width)] for _ in range(height)]

        for (x,y,_,_) in robots:
            grid[y][x] = '#'

        for line in grid:
            print("".join(line))

        input(f'n={iter}')
        next_stop += 10403

    robots = list(map(iter_robot, robots))
    iter += 1

# 172 vert (period 101)
#
# 016 horiz (period 103)
#
# 172 - 16 = 156
# 172 + 156/2*101
#
# 8050 = 172 + 101*78
#
# 101 * 103 = 10403
