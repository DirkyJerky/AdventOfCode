from pathlib import Path
from multiset import Multiset
import re
import networkx as nx


def parse():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    for line in input:
        [total, components] = line.split(':')
        components = list(map(int, components.strip().split(' ')))
        yield (int(total), components)

def is_valid(unit: tuple[int, list[int]]):
    (total, components) = unit

    possible_values = { components[0] }

    for val in components[1:]:
        new_values = set()

        for prev in possible_values:
            new_values.add(val * prev)
            new_values.add(val + prev)

        possible_values = new_values

    return total in possible_values

assert is_valid((190, [19, 10]))
assert is_valid((190, [190, 0]))
assert not is_valid((190, [19, 11]))

total = 0

for unit in parse():
    if is_valid(unit):
        total += unit[0]

print('7a', total)

def is_valid_v2(unit: tuple[int, list[int]]):
    (total, components) = unit

    possible_values = { components[0] }

    for val in components[1:]:
        new_values = set()

        for prev in possible_values:
            new_values.add(val * prev)
            new_values.add(val + prev)
            new_values.add(int(str(prev) + str(val)))

        possible_values = new_values

    return total in possible_values

assert is_valid_v2((190, [19, 0]))

total_2 = 0

for unit in parse():
    if is_valid_v2(unit):
        total_2 += unit[0]

print('7b', total_2)
