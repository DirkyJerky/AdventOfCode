from pathlib import Path
from multiset import Multiset
import re

with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
    input = input_file.readlines()

width = len(input[0])
height = len(input)

offsets = [
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,1), (2,2), (3,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (1,-1), (2,-2), (3,-3)],
    [(0,0), (0,-1), (0,-2), (0,-3)],
    [(0,0), (-1,-1), (-2,-2), (-3,-3)],
    [(0,0), (-1,0), (-2,0), (-3,0)],
    [(0,0), (-1,1), (-2,2), (-3,3)],
]

# offsets = []

# for x_offset in [-1, 0, 1]:
#     for y_offset in [-1, 0, 1]:
#         if
#         pattern = []
#         for i in range()

found_xmases = 0

for x_origin in range(width):
    for y_origin in range(height):
        for offset_pattern in offsets:
            last_offset = offset_pattern[3]

            final_offset_x = x_origin + last_offset[0]
            final_offset_y = y_origin + last_offset[1]

            if final_offset_x < 0:
                continue
            elif final_offset_x >= width:
                continue
            elif final_offset_y < 0:
                continue
            elif final_offset_y >= height:
                continue

            [(x_0, y_0), (x_1, y_1), (x_2, y_2), (x_3, y_3)] = offset_pattern

            if (
                    input[y_origin + y_0][x_origin + x_0] == 'X'
                and input[y_origin + y_1][x_origin + x_1] == 'M'
                and input[y_origin + y_2][x_origin + x_2] == 'A'
                and input[y_origin + y_3][x_origin + x_3] == 'S'
            ):
                # print(x_origin, y_origin)
                found_xmases += 1

print('4a', found_xmases)

found_xxmasses = 0

for x_origin in range(1, width-1):
    for y_origin in range(1, height-1):
        if input[y_origin][x_origin] != 'A':
            continue

        found_m = 0
        found_s = 0

        for x_off in [-1, 1]:
            for y_off in [-1, 1]:
                char = input[y_origin + y_off][x_origin + x_off]

                if char == 'M':
                    found_m += 1
                elif char == 'S':
                    found_s += 1

        if (
            found_m == 2
            and found_s == 2
            and input[y_origin + 1][x_origin + 1] != input[y_origin - 1][x_origin - 1]
        ):
            found_xxmasses += 1

print('4b', found_xxmasses)
