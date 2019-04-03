class Product:
    def __init__(self, name, standard_price, discount_price=None):
        self.name = name
        self.standard_price = standard_price
        self.discount_price = discount_price

    def set_discount(self, discount_amount):
        self.discount_price = self.standard_price - discount_amount

