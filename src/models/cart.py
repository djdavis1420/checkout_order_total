import copy


class Cart():
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
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
