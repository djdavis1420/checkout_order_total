class Product:
    def __init__(self, name, unit_price, unit_weight=1):
        self.name = name
        self.unit_price = unit_price
        self.unit_weight = unit_weight
        self.has_special = False
        self.special_details = None
        self.discount_price = None
        self.sale_price = None

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def calculate_product_cost(self):
        use_price = self.discount_price if self.discount_price is not None else self.unit_price
        self.sale_price = round((float(use_price) * float(self.unit_weight)), 2)
        return self.sale_price
