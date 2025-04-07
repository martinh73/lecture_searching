import os

from setuptools.dist import sequence

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, key):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, string),
    """
    #file_path = os.path.join(cwd_path, file_name)
    import json
    file_name = "sequential.json"
    key = "unordered_numbers"

    with open(file_name) as f:
        data = json.load(f)
        if key in data:
            return data[key]
        else:
            return None
print(read_data(file_name='sequence.json', key='unordered_numbers'))

def linear_search(numbers, searched_number):
    positions = []
    count = 0
    d = dict()
    for index, number in enumerate(numbers):
        if number == searched_number:
            positions.append(index)
            count += 1
        else:
            continue
    return positions, len(positions)
print(linear_search(numbers=[5, 3, 5, 7, 1], searched_number=5))




def main():
    pass


if __name__ == '__main__':
    main()