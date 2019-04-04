import copy


class Cart():
    def __init__(self):
        self.products = []
        self.scanned = []

    def add_product(self, store, product, quantity):
        if store.is_product_available(product):
            while quantity > 0:
                self.products.append(copy.deepcopy(product))
                quantity -= 1

    def remove_product(self, product, quantity):
        while quantity > 0:
            for item in self.products:
                if item.name == product.name:
                    self.products.remove(item)
                    quantity -= 1
                    break
