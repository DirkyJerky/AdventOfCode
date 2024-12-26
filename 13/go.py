from pathlib import Path
import numpy as np
import networkx as nx
import re
import math

from numpy.linalg import LinAlgError

def parse():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    regex = re.compile(r'.*?(\d+).*?(\d+).*')
    for i in range(0, len(input), 4):
        [A_x, A_y] = regex.match(input[i]).groups()
        [B_x, B_y] = regex.match(input[i+1]).groups()
        [X_tot, Y_tot] = regex.match(input[i+2]).groups()

        yield (np.array([[A_x, B_x],[A_y, B_y]], dtype=int), np.array([[X_tot],[Y_tot]], dtype=int))

tokens = 0
tokens_2 = 0

for (arr, sol) in parse():
    # print(arr)
    # print(sol)
    try:
        solve = np.linalg.inv(arr) @ sol
        A = solve[(0,0)]
        B = solve[(1,0)]
        math.isclose(A, round(A))
        if (
            math.isclose(A, round(A))
            and math.isclose(B, round(B))
            and 0 <= A <= 100
            and 0 <= B <= 100
        ):
            # print(solve)
            tokens += 3*solve[(0,0)]
            tokens += 1*solve[(1,0)]
    except LinAlgError:
        print('err', arr, sol)
        pass

    try:
        sol[(0,0)] += 10_000_000_000_000
        sol[(1,0)] += 10_000_000_000_000
        solve = np.linalg.inv(arr) @ sol
        A = solve[(0,0)]
        B = solve[(1,0)]
        if (
            math.isclose(A, round(A), rel_tol=0, abs_tol=0.001)
            and math.isclose(B, round(B), rel_tol=0, abs_tol=0.001)
        ):
            # print(A,B)
            tokens_2 += 3*A + B
    except LinAlgError:
        print('err', arr, sol)
        pass

print('13a', int(tokens))
print('13b', int(tokens_2))
