import copy

from src.models import specials


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

    def total_standard_items(self):
        for item in self.standard_items:
            self.total += item.calculate_product_cost()

    def total_special_items(self):
        unique_products = {item for item in self.special_items}
        for item in unique_products:
            if item.special_details['specialType'] == 'basic unit discount':
                self.total += specials.basic_unit_discount(self, item.name)
            elif item.special_details['specialType'] == 'buy x get y':
                self.total += specials.buy_x_get_y(self, item.name)
            elif item.special_details['specialType'] == 'buy x for y':
                self.total += specials.buy_x_for_y(self, item.name)

    def total_all_items(self):
        self.total_standard_items()
        self.total_special_items()
        return round(self.total, 2)
