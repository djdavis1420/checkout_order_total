from mock import patch

from src.models import specials
from src.models.cart import Cart
from src.models.product import Product
from src.models.store import Store


class TestSpecial:

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

    @patch('src.models.specials.get_special')
    def test_basic_unit_discount__should_total_five_items_with_basic_unit_discount(self, mock_special):
        self.cart.standard_items = self.cheeses + self.beefs
        self.cart.special_items = self.soups + self.sodas + self.soaps
        item_name = 'soup'
        special_details = {'specialType': 'basic unit discount', 'perUnitDiscount': 0.20, 'limit': 5}
        mock_special.return_value = special_details
        actual = specials.basic_unit_discount(self.cart, item_name)
        assert actual == 8.45

    @patch('src.models.specials.get_special')
    def test_basic_unit_discount__should_total_five_items_with_basic_unit_discount_and_one_without_basic_unit_discount_due_to_limit_of_five(self, mock_special):
        self.cart.standard_items = self.cheeses + self.beefs
        self.cart.special_items = self.soups + self.sodas + self.soaps + [self.soup]
        item_name = 'soup'
        special_details = {'specialType': 'basic unit discount', 'perUnitDiscount': 0.20, 'limit': 5}
        mock_special.return_value = special_details
        actual = specials.basic_unit_discount(self.cart, item_name)
        assert actual == 10.34
