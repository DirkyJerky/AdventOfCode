from pathlib import Path
from multiset import Multiset

with open(Path.cwd() / 'input.txt', 'r') as input_file:
    input = input_file.readlines()

list1: list[int] = []
list2: list[int] = []

for line in input:
    [item1, item2] = line.split()
    list1.append(int(item1))
    list2.append(int(item2))

list1.sort()
list2.sort()

assert len(list1) == len(list2)

total_diff = 0

for [comp1, comp2] in zip(list1, list2):
    total_diff += abs(comp1 - comp2)

print('1a', total_diff)

right_multiset: Multiset[int] = Multiset(list2)

total_similarity: int = 0

for item1 in list1:
    total_similarity += item1 * right_multiset.get(item1, 0)

print('1b', total_similarity)
