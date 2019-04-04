from src.checkout import *
from src.models.cart import Cart
from src.models.product import Product


class Test:

    def setup_method(self):
        self.cart = Cart()
        self.soup = Product('soup', 1.89)
        self.soda = Product('soda', 1.49)
        self.soap = Product('soap', 2.49)
        self.beef = Product('beef', 5.99, .75)
        self.bananas = Product('bananas', 2.38, 1)
        self.bananas.set_discount(.15)
        self.cart.add_product(self.soup, 5)
        self.cart.add_product(self.soda, 7)
        self.cart.add_product(self.soap, 4)
        self.cart.add_product(self.beef, 1)
        self.cart.add_product(self.bananas, 2)

    def test_basic_checkout_should_total_items_in_cart(self):
        actual = basic_checkout(self.cart)
        assert actual == 38.79
