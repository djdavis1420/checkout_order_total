import json


def get_special(item_name):
    path = 'C://Users//djdav//Development//Python//checkout_order_total//src//database//specials.json'
    with open(path, 'r') as fileref:
        specials = json.load(fileref)
        for special in specials:
            if special['specialItem'] == item_name:
                return special['specialDetails']

def create_special():
    pass
