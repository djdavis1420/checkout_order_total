from src.models.store import Store
from src.models.cart import Cart
from src.models.product import Product


class TestCart:

    def setup_method(self):
        self.store = Store()
        self.cart = Cart()
        self.soup = Product('soup', 1.89)
        self.soup.has_special = True
        self.soup.special_details = {'specialType': 'basic unit discount', 'perUnitDiscount': 0.20, 'limit': 5}
        self.soda = Product('soda', 1.49)
        self.soda.has_special = True
        self.soda.special_details = {'specialType': 'buy x get y', 'x': 2, 'y': 1, 'z': 100, 'limit': 2}
        self.soap = Product('soap', 2.49)
        self.soap.has_special = True
        self.soap.special_details = {'specialType': 'buy x for y', 'x': 3, 'y': 5, 'limit': 2}
        self.beef = Product('beef', 5.99, 1)
        self.cheese = Product('cheese', 2.38, 1)
        self.store.products = [self.soup, self.soda, self.soap, self.beef, self.cheese]
        self.soups = [self.soup, self.soup, self.soup, self.soup, self.soup]
        self.sodas = [self.soda, self.soda, self.soda, self.soda, self.soda, self.soda]
        self.soaps = [self.soap, self.soap, self.soap, self.soap]
        self.beefs = [self.beef]
        self.cheeses = [self.cheese, self.cheese]
        self.cart.products = self.soups + self.sodas + self.soaps + self.beefs + self.cheeses

    def test_add_product__should_add_one_soup_to_cart(self):
        self.cart.products = []
        self.cart.add_product(self.store, self.soup, 1)
        assert len(self.cart.products) == 1

    def test_add_product__should_add_three_soups_to_cart(self):
        self.cart.products = []
        self.cart.add_product(self.store, self.soup, 3)
        assert len(self.cart.products) == 3

    def test_remove_product__should_remove_one_soup_from_cart_leaving_two(self):
        self.cart.products = [self.soup, self.soup, self.soup]
        self.cart.remove_product(self.soup, 1)
        assert len(self.cart.products) == 2

    def test_remove_product__should_remove_two_soups_from_cart_leaving_one(self):
        self.cart.products = [self.soup, self.soup, self.soup]
        self.cart.remove_product(self.soup, 2)
        assert len(self.cart.products) == 1

    def test_basic_checkout__should_total_items_in_cart(self):
        actual = self.cart.basic_checkout()
        assert actual == 39.10
        assert len(self.cart.products) == 18

    def test_parse_cart__should_divide_items_into_standard_items_and_special_items(self):
        self.cart.parse_cart()
        assert len(self.cart.standard_items) == 3
        assert len(self.cart.special_items) == 15
