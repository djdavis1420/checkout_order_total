class Product:
    def __init__(self, name, standard_price, discount_price=None):
        self.name = name
        self.standard_price = standard_price
        self.discount_price = discount_price
        self.sale_price = 0

    def set_discount(self, discount_amount):
        self.discount_price = self.standard_price - discount_amount

    def calculate_cost(self, weight):
        use_price = self.discount_price if self.discount_price is not None else self.standard_price
        self.sale_price = round((use_price * weight),  2)
        return self.sale_price
