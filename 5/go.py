from pathlib import Path
from multiset import Multiset
import re
import networkx as nx

with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
    input = input_file.readlines()

sep = input.index('\n')

rules = input[:sep]
updates = input[sep+1:]

all_rules: dict[int, set[int]] = {}

dg = nx.DiGraph()

for rule in rules:
    [lhs, rhs] = rule.split('|')

    lhs = int(lhs)
    rhs = int(rhs)

    if lhs not in all_rules:
        all_rules[lhs] = set()

    if rhs not in all_rules:
        all_rules[rhs] = set()

    all_rules[lhs].add(rhs)

    dg.add_edge(lhs, rhs)

total_middles = 0
total_bad_middles = 0

def is_valid(nums):
    for lhs in range(len(nums)):
        for rhs in range(lhs+1, len(nums)):
            if nums[lhs] in all_rules[nums[rhs]]:
                return False
    return True

for update in updates:
    nums = list(map(int, update.split(',')))
    if is_valid(nums):
        total_middles += nums[len(nums) // 2]
    else:

        sub_graph = nx.subgraph(dg, nums)

        new_update = []

        for node in nx.topological_sort(sub_graph):
            new_update.append(node)

        total_bad_middles += new_update[len(new_update) // 2]

print('5a', total_middles)

print('5b', total_bad_middles)
