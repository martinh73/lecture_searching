import json
from itertools import count
from pathlib import Path


def read_data(file_name, key):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, string),
    """
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None
    else:
        with open(file_path, mode="r") as file:
            data = json.load(file)
        return data[key]

def linear_search(numbers, searched_number):

    count = 0
    positions = []

    for i, number in enumerate(numbers):
        if number == searched_number:
            positions.append(i)
            count += 1
        else:
            continue
    return {
        "positions": positions,
        "count": count
    }


def binary_search():




#  #def pattern_search(sequence, pattern):
# sequence = 'ATGACGGAATATAAGCTAGGTGGTGGCTGGGCAGTCCGCGCTGATAGGGCAAGAGTGCGCGTACCATACCACGCTAAGCCATATAGGGCATCAGTCAGCCTGGCA'
# pattern = 'AT'
# n = len(sequence)
# m = len(pattern)
# count = 0
# position = set()
# for index in range (n - (m - 1)):
#     is_same = True
#
#     if sequence[index: index + n] == pattern:
#         count += 1
#     for index_pattern in range(m):
#         print(sequence[index + index_pattern])
#         if sequence[index + index_pattern] != pattern[index_pattern]:
#             is_same = False
#     if is_same:
#         position.add(index)
#     print(position)
#     print(count)
#     print(is_same)




def main():
    pass


if __name__ == '__main__':
    main()