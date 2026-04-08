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


def binary_search(numbers, searched_number):
    middle = len(numbers) // 2
    left_margin = numbers[0]
    right_margin = numbers[-1]
    while len(numbers) != 0:
        if middle == searched_number:
            return middle
        elif middle < searched_number:
            numbers = numbers[middle:right_margin]
        elif middle > searched_number:
            numbers = numbers[left_margin:middle]
    return None


import time

numbers = [4, 8, 15, 16, 23, 42, 55, 78, 91, 120]
target = 78

start = time.perf_counter()

for number in numbers:
    if number == target:
        break

end = time.perf_counter()

duration = end - start
print(f"Měření trvalo {duration:.8f} s")

def pattern_search(sequence, pattern):
    n = len(sequence)
    m = len(pattern)
    count = 0
    position = []
    for i in range (n - (m - 1)):
        is_same = True

        if sequence[i: i + n] == pattern:
            count += 1
        for index_pattern in range(m):
            if sequence[i + index_pattern] != pattern[index_pattern]:
                is_same = False
        if is_same:
            position.append(i)





def main():
    sequential = read_data("sequential.json", "unordered_numbers")
    print(sequential)
    linear = linear_search("sequential.json", "unordered_numbers")
    print(linear)
    binary = binary_search("sequential.json", "unordered_numbers")
    print(binary)

if __name__ == '__main__':
    main()