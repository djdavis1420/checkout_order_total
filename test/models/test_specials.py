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
        self.cart.standard_items = self.cheeses + self.beefs
        self.cart.special_items = self.soups + self.sodas + self.soaps

    @patch('src.models.specials.get_special')
    def test_basic_unit_discount__should_total_five_items_with_basic_unit_discount(self, mock_special):
        item_name = 'soup'
        special_details = {'specialType': 'basic unit discount', 'perUnitDiscount': 0.20, 'limit': 5}
        mock_special.return_value = special_details
        actual = specials.basic_unit_discount(self.cart, item_name)
        assert actual == 8.45

    @patch('src.models.specials.get_special')
    def test_basic_unit_discount__should_total_five_items_with_basic_unit_discount_and_one_without_basic_unit_discount_due_to_limit_of_five(self, mock_special):
        self.cart.special_items += [self.soup]
        item_name = 'soup'
        special_details = {'specialType': 'basic unit discount', 'perUnitDiscount': 0.20, 'limit': 5}
        mock_special.return_value = special_details
        actual = specials.basic_unit_discount(self.cart, item_name)
        assert actual == 10.34

    @patch('src.models.specials.get_special')
    def test_buy_some_get_some__should_buy_two_get_one_free_twice(self, mock_special):
        item_name = 'soda'
        special_details = {'specialType': 'buy some get some', 'buyAmount': 2, 'getAmount': 1, 'percentOff': 100, 'limit': 2}
        mock_special.return_value = special_details
        actual = specials.buy_some_get_some(self.cart, item_name)
        assert actual == 5.96

    @patch('src.models.specials.get_special')
    def test_buy_some_get_some__should_buy_three_get_one_free_with_two_extra(self, mock_special):
        item_name = 'soda'
        special_details = {'specialType': 'buy some get some', 'buyAmount': 3, 'getAmount': 1, 'percentOff': 100, 'limit': 2}
        mock_special.return_value = special_details
        actual = specials.buy_some_get_some(self.cart, item_name)
        assert actual == 7.45

    @patch('src.models.specials.get_special')
    def test_buy_some_get_some__should_buy_two_get_one_half_off_twice(self, mock_special):
        item_name = 'soda'
        special_details = {'specialType': 'buy some get some', 'buyAmount': 2, 'getAmount': 1, 'percentOff': 50, 'limit': 2}
        mock_special.return_value = special_details
        actual = specials.buy_some_get_some(self.cart, item_name)
        assert actual == 7.45

    @patch('src.models.specials.get_special')
    def test_buy_some_get_some__should_buy_two_get_one_free_with_three_extra(self, mock_special):
        item_name = 'soda'
        special_details = {'specialType': 'buy some get some', 'buyAmount': 2, 'getAmount': 1, 'percentOff': 100, 'limit': 1}
        mock_special.return_value = special_details
        actual = specials.buy_some_get_some(self.cart, item_name)
        assert actual == 7.45

    @patch('src.models.specials.get_special')
    def test_buy_some_get_some__should_buy_two_get_one_half_off_with_three_extra(self, mock_special):
        item_name = 'soda'
        special_details = {'specialType': 'buy some get some', 'buyAmount': 2, 'getAmount': 1, 'percentOff': 50, 'limit': 1}
        mock_special.return_value = special_details
        actual = specials.buy_some_get_some(self.cart, item_name)
        assert actual == 8.20

    @patch('src.models.specials.get_special')
    def test_buy_some_get_some__should_buy_two_get_one_half_off_twice_due_to_limit_of_0(self, mock_special):
        item_name = 'soda'
        special_details = {'specialType': 'buy some get some', 'buyAmount': 2, 'getAmount': 1, 'percentOff': 50, 'limit': 0}
        mock_special.return_value = special_details
        actual = specials.buy_some_get_some(self.cart, item_name)
        assert actual == 7.45

    @patch('src.models.specials.get_special')
    def test_buy_some_get_some__should_buy_two_get_one_half_off_twice_due_to_limit_of_none(self, mock_special):
        item_name = 'soda'
        special_details = {'specialType': 'buy some get some', 'buyAmount': 2, 'getAmount': 1, 'percentOff': 50, 'limit': None}
        mock_special.return_value = special_details
        actual = specials.buy_some_get_some(self.cart, item_name)
        assert actual == 7.45

    @patch('src.models.specials.get_special')
    def test_buy_some_for_amount__should_buy_three_for_five_with_one_extra(self, mock_special):
        item_name = 'soap'
        special_details = {'specialType': 'buy some for amount', 'buyAmount': 3, 'dollarAmount': 5, 'limit': 2}
        mock_special.return_value = special_details
        actual = specials.buy_some_for_amount(self.cart, item_name)
        assert actual == 7.49

    @patch('src.models.specials.get_special')
    def test_buy_some_for_amount__should_buy_three_for_five_with_two_extra(self, mock_special):
        self.cart.special_items += [self.soap]
        item_name = 'soap'
        special_details = {'specialType': 'buy some for amount', 'buyAmount': 3, 'dollarAmount': 5, 'limit': 2}
        mock_special.return_value = special_details
        actual = specials.buy_some_for_amount(self.cart, item_name)
        assert actual == 9.98

    @patch('src.models.specials.get_special')
    def test_buy_some_for_amount__should_buy_three_for_five_twice(self, mock_special):
        self.cart.special_items += [self.soap, self.soap]
        item_name = 'soap'
        special_details = {'specialType': 'buy some for amount', 'buyAmount': 3, 'dollarAmount': 5, 'limit': 2}
        mock_special.return_value = special_details
        actual = specials.buy_some_for_amount(self.cart, item_name)
        assert actual == 10.00

    @patch('src.models.specials.get_special')
    def test_buy_some_for_amount__should_buy_three_for_five_twice_with_two_extra_due_to_limit_of_two(self, mock_special):
        self.cart.special_items += [self.soap, self.soap, self.soap, self.soap]
        item_name = 'soap'
        special_details = {'specialType': 'buy some for amount', 'buyAmount': 3, 'dollarAmount': 5, 'limit': 2}
        mock_special.return_value = special_details
        actual = specials.buy_some_for_amount(self.cart, item_name)
        assert actual == 14.98

    @patch('src.models.specials.get_special')
    def test_buy_some_for_amount__should_buy_three_for_five_twice_with_three_extra_due_to_limit_of_two(self, mock_special):
        self.cart.special_items += [self.soap, self.soap, self.soap, self.soap, self.soap]
        item_name = 'soap'
        special_details = {'specialType': 'buy some for amount', 'buyAmount': 3, 'dollarAmount': 5, 'limit': 2}
        mock_special.return_value = special_details
        actual = specials.buy_some_for_amount(self.cart, item_name)
        assert actual == 17.47

    @patch('src.models.specials.get_special')
    def test_buy_some_for_amount__should_buy_three_for_five_twice_with_four_extra_due_to_limit_of_two(self, mock_special):
        self.cart.special_items += [self.soap, self.soap, self.soap, self.soap, self.soap, self.soap]
        item_name = 'soap'
        special_details = {'specialType': 'buy some for amount', 'buyAmount': 3, 'dollarAmount': 5, 'limit': 2}
        mock_special.return_value = special_details
        actual = specials.buy_some_for_amount(self.cart, item_name)
        assert actual == 19.96

    @patch('src.models.specials.get_special')
    def test_buy_some_for_amount__should_buy_four_for_five_once_with_six_extra_due_to_limit_of_one(self, mock_special):
        self.cart.special_items += [self.soap, self.soap, self.soap, self.soap, self.soap, self.soap]
        item_name = 'soap'
        special_details = {'specialType': 'buy some for amount', 'buyAmount': 4, 'dollarAmount': 5, 'limit': 1}
        mock_special.return_value = special_details
        actual = specials.buy_some_for_amount(self.cart, item_name)
        assert actual == 19.94
