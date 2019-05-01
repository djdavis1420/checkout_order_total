from src.models.product import Product
import os


def get_all_products():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'products.csv')
    with open(filename, 'r') as fileref:
        product_list = fileref.readlines()
        return [create_product(product) for product in product_list[1:]]


def create_product(product):
    item = product.strip().split(',')
    return Product(item[0], float(item[1]), int(item[2]))
