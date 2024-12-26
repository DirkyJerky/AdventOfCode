from pathlib import Path
from networkx.exception import NetworkXNoPath
import numpy as np
import networkx as nx
from functools import cache

def parse():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    split = input.index('\n')

    towels = set(map(lambda s: s.strip(), "".join(input[0:split]).strip().split(',')))
    goals = input[(split+1):]

    return (towels, goals)

(towels, goals) = parse()
# print(towels)

max_size = max(map(len, towels))

num_achievable = 0

@cache
def is_viable(goal):
    # print(goal)
    if goal == '':
        return True
    for pfx_length in range(1, max_size+1):
        pfx = goal[:pfx_length]
        # print(pfx)
        if pfx in towels:
            # print('in')
            if is_viable(goal[pfx_length:]):
                return True
    return False

for goal in goals:
    # print(goal)
    if is_viable(goal.strip()):
        num_achievable += 1
        # print(num_achievable)

print('19a', num_achievable)

num_options = 0

@cache
def is_viable_v2(goal):
    if goal == '':
        return 1

    num = 0
    for pfx_length in range(1, min(max_size+1, len(goal)+1)):
        pfx = goal[:pfx_length]
        # print(pfx)
        if pfx in towels:
            # print('in')
            num += is_viable_v2(goal[pfx_length:])
    # print(goal, num)
    return num

total = 0

for goal in goals:
    # print(goal)
    total += is_viable_v2(goal.strip())

print('19b', total)
