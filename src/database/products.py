from src.models.product import Product


def get_all_products():
    path = 'C://Users//djdav//Development//Python//checkout_order_total//src//database//products.csv'
    with open(path, 'r') as fileref:
        product_list = fileref.readlines()

        return [create_product(product) for product in product_list[1:]]


def create_product(product):
    item = product.strip().split(',')
    return Product(item[0], float(item[1]), int(item[2]))
