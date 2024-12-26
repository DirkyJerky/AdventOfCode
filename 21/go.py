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

codes = parse()

# (dy,dx)
direction_map = {
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
}

def is_valid(shape : tuple, index : tuple):
    return (0 <= index[0] < shape[0] and
        0 <= index[1] < shape[1])

class Keypad:
    def __init__(self, grid):
        grid = np.array(grid)

        self.grid = nx.DiGraph()

        for (y,x), chr in np.ndenumerate(grid):
            assert isinstance(chr, str)
            if chr == ' ':
                continue

            for dir, (dy,dx) in direction_map.items():
                adj = (y+dy,x+dx)
                if is_valid(grid.shape, adj) and grid[adj] != ' ':
                    self.grid.add_edge(chr, grid[adj], dir=dir)

    @cache
    def input_char(self, frm: str, to: str) -> list[str]:
        paths = nx.all_shortest_paths(self.grid, frm, to)
        all_dirs = []
        for path in paths:
            dirs = ''
            for i in range(len(path)-1):
                dirs += self.grid.get_edge_data(path[i], path[i+1])['dir']
            dirs += 'A'
            all_dirs.append(dirs)
        return all_dirs

    @cache
    def input_string(self, frm: str, s: str, optimize_with = None) -> list[str]:
        if not len(s):
            return ['']
            return

        instrs = self.input_char(frm, s[0])
        rests = self.input_string(s[0], s[1:])

        all_instrs = []

        for instr in instrs:
            # print('instr', instr)
            for rest in rests:
                # print('rest', rest)
                all_instrs.append(instr + rest)

        if optimize_with:
            assert isinstance(optimize_with, Keypad)
            min_instr = None
            len_toplevel = None
            for instr in all_instrs:
                for top_level_instr in optimize_with.input_string('A', instr):
                    for top_level_instr2 in optimize_with.input_string('A', instr):
                        if not len_toplevel or len(top_level_instr2) < len_toplevel:
                            min_instr = instr

            assert min_instr
            all_instrs = [min_instr]

        return all_instrs

num_keypad = Keypad(
    [
        ['7','8','9'],
        ['4','5','6'],
        ['1','2','3'],
        [' ','0','A']
    ]
)

dir_keypad = Keypad(
    [
        [' ','^','A'],
        ['<','v','>'],
    ]
)

assert list(num_keypad.input_string('A','A')) == ['A']
assert list(num_keypad.input_string('A','3')) == ['^A']
assert list(num_keypad.input_string('3','A')) == ['vA']
assert list(num_keypad.input_string('A','9')) == ['^^^A']
assert list(num_keypad.input_string('9','5')) == ['<vA', 'v<A']
assert list(num_keypad.input_string('5','2')) == ['vA']
assert list(num_keypad.input_string('2','A')) == ['v>A', '>vA']

assert list(num_keypad.input_string('A','1')) == ['<^<A','^<<A']
assert list(num_keypad.input_string('A','1', dir_keypad)) == ['^<<A']

def make_transition_map(s: str, existing: dict[tuple[str, str], int] | None = None, mult: int = 1) -> dict[tuple[str, str], int]:
    transitions = existing or {}

    for (frm, to) in zip('A'+s[:-1],s):
        if (frm,to) not in transitions:
            transitions[(frm,to)] = 0
        transitions[(frm,to)] += mult

    return transitions

# def print_transition_map(transitions: dict[tuple[str, str], int]):
#     for (frm, to), num in transitions.items():
#         print(f'{frm} -> {to}: {num}')

#     print('total', sum(transitions.values()))

def get_min_instr(code: str) -> str:
    min = None
    for numpad_instr in num_keypad.input_string('A',code):
        for dirpad_instr1 in dir_keypad.input_string('A',numpad_instr):
            for dirpad_instr2 in dir_keypad.input_string('A',dirpad_instr1):
                if not min or len(min) > len(dirpad_instr2):
                    min = dirpad_instr2
                    # print(f'found len {len(min)}')
                    # print(f'found numpad_instr {numpad_instr}')
                    # print_transition_map(make_transition_map(numpad_instr))
                    # print(f'found dirpad_instr1 {dirpad_instr1}')
                    # print_transition_map(make_transition_map(dirpad_instr1))
                    # print(f'found dirpad_instr2 {dirpad_instr2}')
                    # print_transition_map(make_transition_map(dirpad_instr2))
    assert min
    return min

complexities = 0
for code in codes:
    instr = get_min_instr(code)

    print('code', code)
    # print('instr', instr)
    print('len', len(instr))
    # print('number', int(code[0:3]))
    # print('complexity', len(instr) * int(code[0:3]))

    complexities += len(instr) * int(code[0:3])

print('21a', complexities)

def run_with_N_keypads(n: int):
    complexities = 0
    for code in codes:
        min = None
        numpad_seqs = num_keypad.input_string('A', code)
        for numpad_seq in numpad_seqs:
            transitions = make_transition_map(numpad_seq)

            # print(0, code)
            # print(numpad_seq)
            # print(transitions)

            for i in range(n):
                # print(i+1)
                new_transitions = {}

                for (frm,to), num in transitions.items():
                    best_seqs = dir_keypad.input_string(frm, to, dir_keypad)
                    assert len(best_seqs) == 1
                    best_seq = best_seqs[0]

                    new_transitions = make_transition_map(best_seq, new_transitions, num)

                transitions = new_transitions
                # print_transition_map(transitions)

            if not min or min > sum(transitions.values()):
                min = sum(transitions.values())

        print(code, min)
        assert min
        complexities += min * int(code[0:3])

    return complexities


print('21a', run_with_N_keypads(2))
print('21b', run_with_N_keypads(25))

# (from, to): seq
# transition_map = {
#     ('A', '>'): 'vA',
#     ('A', 'v'): '<vA',
#     ('A', '<'): 'v<<A',
#     ('A', '^'): '<A',
#     ('A', 'A'): 'A',
#     ('v', '>'): '<A',
#     ('v', 'v'): 'A',
#     ('v', '<'): '<A',
#     ('v', '^'): '^A',
#     ('v', 'A'): '^>A',
#     ('>', '>'): 'A',
#     ('>', 'v'): '<A',
#     ('>', '<'): '<<A',
#     ('>', '^'): '<^A',
#     ('>', 'A'): '^A',
#     ('^', '>'): 'v>A',
#     ('^', 'v'): 'vA',
#     ('^', '<'): 'v<A',
#     ('^', '^'): 'A',
#     ('^', 'A'): '>A',
#     ('<', '>'): '>>A',
#     ('<', 'v'): '>A',
#     ('<', '<'): 'A',
#     ('<', '^'): '>^A',
#     ('<', 'A'): '>>^A'
# }

# def run_with_N_keypads(n: int):
#     complexities = 0
#     for code in codes:
#         min = None
#         numpad_seqs = num_keypad.input_string('A', code)
#         for numpad_seq in numpad_seqs:
#             transitions = make_transition_map(numpad_seq)

#             # print(0, code)
#             # print(numpad_seq)
#             # print(transitions)

#             for i in range(n):
#                 # print(i+1)
#                 new_transitions = {}

#                 for (frm,to), num in transitions.items():
#                     new_transitions = make_transition_map(transition_map[(frm,to)], new_transitions, num)

#                 transitions = new_transitions
#                 # print_transition_map(transitions)

#             if not min or min > sum(transitions.values()):
#                 min = sum(transitions.values())

#         print(code, min)
#         assert min
#         complexities += min * int(code[0:3])

#     return complexities

# print('21a', run_with_N_keypads(2))
# print('21b', run_with_N_keypads(25))
