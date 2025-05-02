from pathlib import Path
from typing import Generator
import numpy as np
import networkx as nx
from numpy._typing import NDArray
from functools import cache

def parse():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    return list(map(lambda l: l.strip(), input))

initials = list(map(int, parse()))

def to_mix(secret, val):
    return secret ^ val

assert to_mix(42, 15) == 37

def to_prune(secret):
    return secret % 16777216

assert to_prune(100000000) == 16113920

def get_next(secret: int):
    num = to_prune(to_mix(secret, secret << 6)) #   * 64
    num = to_prune(to_mix(num, num >> 5)) #   // 32
    num = to_prune(to_mix(num, num << 11)) #  * 2048
    return num

test = [
    123,
    15887950,
    16495136,
    527345,
    704524,
    1553684,
    12683156,
    11100544,
    12249484,
    7753432,
    5908254
]

for i in range(len(test)-1):
    assert get_next(test[i]) == test[i+1]

total_a = 0
for initial in initials:
    # print(initial)
    num = initial
    for i in range(2000):
        num = get_next(num)

    # print(num)
    total_a += num

print('21a', total_a)

totals_map = {}

for initial in initials:
    # print(initial)
    num = initial

    diff_map: dict[str, int] = {}

    diffs = []

    for i in range(2000):
        nxt = get_next(num)

        diffs.append((nxt % 10) - (num % 10))
        diffs = diffs[-4:]
        key = "".join(map(str,diffs))

        if key not in diff_map:
            diff_map[key] = nxt % 10

        num = nxt

    for key, value in diff_map.items():
        if key not in totals_map:
            totals_map[key] = 0

        totals_map[key] += value

print('21b', max(totals_map.values()))
