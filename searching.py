import os

from setuptools.dist import sequence

# get current working directory path
cwd_path = os.getcwd()


# def read_data(file_name, key):
#     """
#     Reads json file and returns sequential data.
#     :param file_name: (str), name of json file
#     :param key: (str), field of a dict to return
#     :return: (list, string),
#     """
#     #file_path = os.path.join(cwd_path, file_name)
#     import json
#     file_name = "sequential.json"
#     key = "unordered_numbers"
#
#     with open(file_name) as f:
#         data = json.load(f)
#         if key in data:
#             return data[key]
#         else:
#             return None
# print(read_data(file_name='sequence.json', key='unordered_numbers'))

# def linear_search(numbers, searched_number):
#     positions = []
#     count = 0
#     d = dict()
#     for index, number in enumerate(numbers):
#         if number == searched_number:
#             positions.append(index)
#             count += 1
#         else:
#             continue
#     return positions, len(positions)
# print(linear_search(numbers=[5, 3, 5, 7, 1], searched_number=5))

#def pattern_search(sequence, pattern):
sequence = 'ATGACGGAATATAAGCTAGGTGGTGGCTGGGCAGTCCGCGCTGATAGGGCAAGAGTGCGCGTACCATACCACGCTAAGCCATATAGGGCATCAGTCAGCCTGGCA'
pattern = 'AT'
n = len(sequence)
m = len(pattern)
count = 0
position = set()
for index in range (n - (m - 1)):
    is_same = True

    if sequence[index: index + n] == pattern:
        count += 1
    for index_pattern in range(m):
        print(sequence[index + index_pattern])
        if sequence[index + index_pattern] != pattern[index_pattern]:
            is_same = False
    if is_same:
        position.add(index)
    print(position)
    print(count)
    print(is_same)




def main():
    pass


if __name__ == '__main__':
    main()