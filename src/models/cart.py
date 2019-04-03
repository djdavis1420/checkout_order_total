class Cart():
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        while quantity > 0:
            self.products.append(product)
            quantity -= 1

    def remove_product(self, product, quantity):
        while quantity > 0:
            self.products.remove(product)
            quantity -= 1
