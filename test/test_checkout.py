from src.checkout import Checkout
from src.models.store import Store
from src.models.cart import Cart
from src.models.product import Product


class Test:

    def setup_method(self):
        self.store = Store()
        self.cart = Cart()
        self.soup = Product('soup', 1.89)
        self.soda = Product('soda', 1.49)
        self.soap = Product('soap', 2.49)
        self.beef = Product('beef', 5.99, .75)
        self.bananas = Product('bananas', 2.38, 1)
        self.store.stock_product(self.soup)
        self.store.stock_product(self.soda)
        self.store.stock_product(self.soap)
        self.store.stock_product(self.beef)
        self.store.stock_product(self.bananas)
        self.store.activate_special_on_product(self.soup, 'basic unit discount')
        self.store.activate_special_on_product(self.soda, 'buy x get y')
        self.cart.add_product(self.store, self.soup, 5)
        self.cart.add_product(self.store, self.soda, 7)
        self.cart.add_product(self.store, self.soap, 4)
        self.cart.add_product(self.store, self.beef, 1)
        self.cart.add_product(self.store, self.bananas, 2)
        self.cart.remove_product(self.soda, 2)
        self.checkout = Checkout(self.cart)

    def test_basic_checkout_should_total_items_in_cart(self):
        actual = self.checkout.basic_checkout(self.cart)
        assert actual == 36.11
        assert len(self.cart.scanned) == 17
        assert len(self.cart.products) == 0

    def test_parse_cart__should_divide_items_into_standard_items_and_special_items(self):
        self.checkout.parse_cart(self.cart)
        assert len(self.checkout.standard_items) == 7
        assert len(self.checkout.special_items) == 10

    def test_build_specials__should_build_dictionaries_for_special_items(self):
        self.checkout.parse_cart(self.cart)
        self.checkout.build_specials(self.cart)
        assert len(self.checkout.special_items) == 2
