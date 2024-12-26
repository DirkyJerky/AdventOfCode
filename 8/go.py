from pathlib import Path
from multiset import Multiset
import re
import networkx as nx


def parse_grid():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    width = len(input[0]) - 1
    height = len(input)

    skip_list = {'.'}

    location_dict: dict[str, set[tuple[int, int]]] = {}

    for y, line in enumerate(input):
        for x, chr in enumerate(line):
            if chr not in skip_list:
                if chr not in location_dict:
                    location_dict[chr] = set()

                location_dict[chr].add((x,y))

    return (width, height, location_dict)

(width, height, locations) = parse_grid()

def is_in_grid(unit):
    (x,y) = unit

    return 0 <= x < width and 0 <= y < height

antinodes = set()

for _, locs in locations.items():
    for loc_1 in locs:
        for loc_2 in locs:
            if loc_1 == loc_2:
                continue

            (x_1, y_1) = loc_1
            (x_2, y_2) = loc_2

            x_off = x_2 - x_1
            y_off = y_2 - y_1

            from_1 = (x_1 - x_off, y_1 - y_off)
            from_2 = (x_2 + x_off, y_2 + y_off)

            if is_in_grid(from_1):
                antinodes.add(from_1)

            if is_in_grid(from_2):
                antinodes.add(from_2)

print('8a', len(antinodes))

antinodes = set()

for _, locs in locations.items():
    for loc_1 in locs:
        for loc_2 in locs:
            if loc_1 == loc_2:
                continue

            (x_1, y_1) = loc_1
            (x_2, y_2) = loc_2

            x_off = x_2 - x_1
            y_off = y_2 - y_1

            from_1 = (x_1, y_1)
            while True:
                if is_in_grid(from_1):
                    antinodes.add(from_1)
                    from_1 = (from_1[0] - x_off, from_1[1] - y_off)
                else:
                    break

            from_2 = (x_2, y_2)
            while True:
                if is_in_grid(from_1):
                    antinodes.add(from_2)
                    from_2 = (from_1[0] + x_off, from_2[1] + y_off)
                else:
                    break

print('8b', len(antinodes))
