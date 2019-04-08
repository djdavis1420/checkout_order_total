import copy


class Cart():
    def __init__(self):
        self.products = []
        self.standard_items = []
        self.special_items = []
        self.total = 0

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

    def basic_checkout(self):
        for item in self.products:
            item.calculate_product_cost()
            self.total += item.sale_price
        return round(self.total, 2)

    def parse_cart(self):
        for item in self.products:
            if item.has_special is False:
                self.standard_items.append(item)
            else:
                self.special_items.append(item)
