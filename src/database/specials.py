import json
import os


def get_special(item_name):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'specials.json')
    with open(filename, 'r') as fileref:
        specials = json.load(fileref)
        for special in specials:
            if special['specialItem'] == item_name:
                return special['specialDetails']


def create_special():
    pass
