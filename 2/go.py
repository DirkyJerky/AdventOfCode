from pathlib import Path
from multiset import Multiset

with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
    input = input_file.readlines()

def is_safe(nums):
    diff_list = []

    for i in range(1, len(nums)):
        diff_list.append(nums[i] - nums[i-1])

    if all(map(lambda x: x >= 1 and x <= 3, diff_list)):
        return True
    elif all(map(lambda x: x <= -1 and x >= -3, diff_list)):
        return True
    else:
        return False

num_safe = 0
num_alt_safe = 0

for line in input:
    items = list(map(int, line.split()))
    assert len(items) > 1

    if is_safe(items):
        num_safe += 1
        num_alt_safe += 1
    else:
        for splice_index in range(len(items)):
            if is_safe(items[:splice_index] + items[(splice_index+1):]):
                num_alt_safe += 1
                break

print('2a', num_safe)
print('2b', num_alt_safe)
