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

    def discontinue_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def activate_special_on_product(self, product, special_type):
        for item in self.products:
            if item.name == product.name:
                item.special = special_type
