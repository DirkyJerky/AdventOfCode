from pathlib import Path
import numpy as np

def parse():
    with open(Path(__file__).parent / 'input.txt', 'r') as input_file:
        input = input_file.readlines()

    all_input = "".join(input).strip()
    len_sectors = sum(map(int, all_input))
    file_sectors = np.full(len_sectors, -1)

    empties_list: list[tuple[int, int, int]] = []
    files_list: list[tuple[int, int, int]] = []

    is_file = True
    idx = 0
    id = 0

    for chr in all_input:
        num = int(chr)
        if is_file:
            file_sectors[idx:(idx+num)] = id
            files_list.append((idx, num, id))
            id += 1
        else:
            empties_list.append((idx, num, -1))
        idx += num
        is_file = not is_file

    return (file_sectors, files_list, empties_list)

(sectors, files, empties) = parse()

# print(sectors)

blanks = np.argwhere(sectors == -1)
filled = np.argwhere(sectors >= 0)

# print('blanks', blanks.shape)
# print('filled', filled.shape)

if blanks.shape[0] > filled.shape[0]:
    filled = np.copy(filled)
    filled.resize(blanks.shape)
else:
    blanks = np.copy(blanks)
    blanks.resize(filled.shape)

for [left_blank_idx, right_filled_idx] in np.stack((blanks, filled[::-1]), axis=1):
    if left_blank_idx == 0 or right_filled_idx == 0:
        break
    if left_blank_idx > right_filled_idx:
        break
    sectors[left_blank_idx] = sectors[right_filled_idx]
    sectors[right_filled_idx] = -1


sectors = np.transpose(sectors[np.argwhere(sectors >= 0)])[0]

total = 0

for idx, value in np.ndenumerate(sectors):
    # print(idx, value)
    total += idx[0] * value

print('9a', total)

files.reverse()
for file_unit_idx in range(len(files)):
    (idx_file, len_file, id_file) = files[file_unit_idx]

    for empty_unit_idx in range(len(empties)):
        (idx_empty, len_empty, _) = empties[empty_unit_idx]

        if idx_empty > idx_file:
            continue

        if len_empty >= len_file:
            files[file_unit_idx] = (idx_empty, len_file, id_file)
            empties[empty_unit_idx] = (idx_empty + len_file, len_empty - len_file, -1)
            break

# print(sectors)
# print(files)

total_2 = 0

for file in files:
    (idx, len, id) = file

    for i in range(len):
        total_2 += (idx + i) * id

print('9b', total_2)
