from src.database.products import get_all_products
from src.database.specials import get_special


class Store:
    def __init__(self):
        self.products = []

    def is_product_available(self, product):
        if product not in self.products:
            return False
        return True

    def stock_product(self, product):
        if product not in self.products:
            self.products.append(product)

    def stock_products(self):
        products = get_all_products()
        self.products = products

    def discontinue_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def activate_special_on_product(self, product):
        special_details = get_special(product.name)
        for item in self.products:
            if item.name == product.name:
                item.has_special = True
                item.special_details = special_details
