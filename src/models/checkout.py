class Checkout:

    def __init__(self, cart):
        self.total = 0
        self.cart = cart
        self.standard_items = []
        self.special_items = []

    def basic_checkout(self, cart):
        self.total = 0
        for item in reversed(cart.products):
            item.calculate_product_cost()
            self.total += item.sale_price
            cart.scanned.append(item)
            cart.products.remove(item)
        return round(self.total, 2)

    def parse_cart(self, cart):
        for item in cart.products:
            if item.special_type is False:
                self.standard_items.append(item)
            else:
                self.special_items.append(item)

    def build_specials(self, cart):
        sorted_products = sorted(self.special_items, key=lambda x: x.name)
        unique_item_names = {item.name for item in self.special_items}
        special_items = []

        for item_name in unique_item_names:
            unique_item = {}
            count = 0
            for item in sorted_products:
                if item_name == item.name:
                    unique_item['product_name'] = item.name
                    unique_item['special_type'] = item.special_type
                    unique_item['unit_price'] = item.unit_price
                    count += 1
            unique_item['count'] = count
            special_items.append(unique_item)
        self.special_items = special_items
