from copy import deepcopy
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
        self.soda.special_details = {'specialType': 'buy some get some', 'buyAmount': 2, 'getAmount': 1, 'percentOff': 100, 'limit': 2}
        self.soap = Product('soap', 2.49)
        self.soap.has_special = True
        self.soap.special_details = {'specialType': 'buy some for amount', 'buyAmount': 3, 'dollarAmount': 5, 'limit': 2}
        self.beef = Product('beef', 5.99, 1)
        self.cheese = Product('cheese', 2.38, 1)
        self.store.products = [self.soup, self.soda, self.soap, self.beef, self.cheese]
        self.soups = [self.soup, self.soup, self.soup, self.soup, self.soup]
        self.sodas = [self.soda, self.soda, self.soda, self.soda, self.soda, self.soda]
        self.soaps = [self.soap, self.soap, self.soap, self.soap]
        self.beefs = [self.beef]
        self.cheeses = [self.cheese, self.cheese]
        self.cart.products = self.soups + self.sodas + self.soaps + self.beefs + self.cheeses

    def test_add_product_by_unit__should_add_one_soup_to_cart(self):
        self.cart.products = []
        self.cart.add_product_by_unit(self.store, self.soup, 1)
        assert len(self.cart.products) == 1

    def test_add_product_by_unit__should_add_three_soups_to_cart(self):
        self.cart.products = []
        self.cart.add_product_by_unit(self.store, self.soup, 3)
        assert len(self.cart.products) == 3

    def test_add_product_by_weight__should_add_half_pound_of_beef_to_cart(self):
        self.cart.products = []
        self.cart.add_product_by_weight(self.store, self.beef, .50)
        assert len(self.cart.products) == 1
        assert self.cart.products[0].unit_weight == .5

    def test_remove_product__should_remove_one_soup_from_cart_leaving_two(self):
        self.cart.products = [self.soup, self.soup, self.soup]
        self.cart.remove_product('soup', 1)
        assert len(self.cart.products) == 2

    def test_remove_product__should_remove_two_soups_from_cart_leaving_one(self):
        self.cart.products = [self.soup, self.soup, self.soup]
        self.cart.remove_product('soup', 2)
        assert len(self.cart.products) == 1

    def test_basic_checkout__should_total_items_in_cart(self):
        actual = self.cart.basic_checkout()
        assert actual == 39.10
        assert len(self.cart.products) == 18

    def test_basic_checkout__should_total_half_pound_beef_and_half_pound_cheese(self):
        beef = Product('beef', 5.99, .5)
        cheese = Product('cheese', 2.38, .5)
        self.cart.products = [beef, cheese]
        actual = self.cart.basic_checkout()
        assert actual == 4.19

    def test_parse_cart__should_divide_items_into_standard_items_and_special_items(self):
        self.cart.parse_cart()
        assert len(self.cart.standard_items) == 3
        assert len(self.cart.special_items) == 15

    def test_total_standard_items__should_total_all_standard_items(self):
        self.cart.standard_items = self.cheeses + self.beefs
        self.cart.special_items = self.soups + self.sodas + self.soaps
        self.cart.total_standard_items()
        assert self.cart.total == 10.75

    def test_total_special_items__should_total_all_items_with_active_specials(self):
        self.cart.standard_items = self.cheeses + self.beefs
        self.cart.special_items = self.soups + self.sodas + self.soaps
        self.cart.total_special_items()
        assert self.cart.total == 21.90

    def test_total_all_items__should_return_total_of_standard_items_and_special_items(self):
        self.cart.standard_items = self.cheeses + self.beefs
        self.cart.special_items = self.soups + self.sodas + self.soaps
        actual = self.cart.total_all_items()
        assert actual == 32.65

    # This test overwrites some of TestCart setup in order to test {set} of objects based on object.name
    # The behavior being tested is the deduplication of deep copies of objects based on object.name
    # This behavior is achieved by overwriting __hash__ and __eq__ on Product
    def test_total_special_items__testing_set_of_objects_based_on_object_name(self):
        self.cart.products = []
        self.soups = [deepcopy(self.soup), deepcopy(self.soup), deepcopy(self.soup), deepcopy(self.soup), deepcopy(self.soup)]
        self.sodas = [deepcopy(self.soda), deepcopy(self.soda), deepcopy(self.soda), deepcopy(self.soda), deepcopy(self.soda), deepcopy(self.soda)]
        self.soaps = [deepcopy(self.soap), deepcopy(self.soap), deepcopy(self.soap), deepcopy(self.soap)]
        self.beefs = [deepcopy(self.beef)]
        self.cheeses = [deepcopy(self.cheese), deepcopy(self.cheese)]
        self.cart.products = self.soups + self.sodas + self.soaps + self.beefs + self.cheeses
        self.cart.parse_cart()
        self.cart.total_special_items()
        assert self.cart.total == 21.90
