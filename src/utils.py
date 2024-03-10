import json
from config import ROOT_DIR
from os.path import join

data_path_file = join(ROOT_DIR, 'src', 'operations.json')


def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

