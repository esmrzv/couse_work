
from src.utils import load_file
from config import ROOT_DIR
from os.path import join

data_path = join(ROOT_DIR, 'operations.json')


def test_load_file():
    assert type(load_file(data_path)) == list
