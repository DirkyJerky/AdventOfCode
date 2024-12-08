from pathlib import Path
from multiset import Multiset
import re

with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
    input = "".join(input_file.readlines())

valid_mul = re.compile(r'mul\((\d+),(\d+)\)')

total = 0

for match in valid_mul.finditer(input):
    groups = match.groups()
    assert isinstance(groups[0], str)
    assert isinstance(groups[1], str)
    total += int(groups[0]) * int(groups[1])

print('3a', total)

valid_instrs = re.compile(r'do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)')

mul_enabled = True
total = 0

for match in valid_instrs.finditer(input):
    instr = match.group(0)
    if instr == 'do()':
        mul_enabled = True
    elif instr == 'don\'t()':
        mul_enabled = False
    else:
        if mul_enabled:
            total += int(match.group(1)) * int(match.group(2))

print('3b', total)
