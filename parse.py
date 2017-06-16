import json

from pprint import pprint

def load_json(filename):
    # Loading the data into a list
    data = []
    with open(filename) as data_file:
        for line in data_file:
            data.append(json.loads(line))

    return data