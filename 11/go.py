from operator import ifloordiv
from pathlib import Path
import numpy as np
import networkx as nx

def parse():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    return list(map(int, input[0].strip().split(' ')))

nums_0 = parse()

def iterate_stone(val):
    if (val == 0):
        return [1]

    val_str = str(val)

    len_str = len(val_str)
    if (len_str % 2 == 0):
        half = len_str // 2
        return [int(val_str[:half]), int(val_str[half:])]

    return [2024 * val]

assert iterate_stone(0) == [1]
assert iterate_stone(1) == [2024]
assert iterate_stone(10) == [1, 0]
assert iterate_stone(1000) == [10, 0]
assert iterate_stone(99) == [9, 9]
assert iterate_stone(999) == [2021976]

def iterate_all_stones(vals):

    return [x for stone in vals for x in iterate_stone(stone)]

assert iterate_all_stones([125, 17]) == [253000, 1, 7]
assert iterate_all_stones([253000, 1, 7]) == [253, 0, 2024, 14168]

stones = nums_0
for i in range(25):
    stones = iterate_all_stones(stones)

print('11a', len(stones))

def improved_iterate_all_stones(vals: dict[int, int]):
    new_dict: dict[int, int] = {}

    for val, quantity in vals.items():
        for res in iterate_stone(val):
            if res not in new_dict:
                new_dict[res] = 0

            new_dict[res] += quantity

    return new_dict

dict_0 = {}
for num in nums_0:
    dict_0[num] = 1

dict_iter = dict_0
for i in range(25):
    # print(i)
    dict_iter = improved_iterate_all_stones(dict_iter)

print('11a', sum(dict_iter.values()))

dict_iter = dict_0
for i in range(75):
    # print(i)
    dict_iter = improved_iterate_all_stones(dict_iter)

print('11b', sum(dict_iter.values()))
