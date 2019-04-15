from mock import patch

from src.models.store import Store
from src.models.product import Product


class TestStore:

    def setup_method(self):
        self.store = Store()
        self.soup = Product('soup', 1.89)
        self.beef = Product('beef', 5.99)

    def test_is_product_available__should_be_false_if_list_is_empty(self):
        actual = self.store.is_product_available('soup')
        assert actual is False

    def test_is_product_available__should_be_false_if_item_not_in_list(self):
        self.store.products = [self.beef]
        actual = self.store.is_product_available('soup')
        assert actual is False

    def test_is_product_available__should_be_true(self):
        self.store.products = [self.soup]
        actual = self.store.is_product_available('soup')
        assert actual is True

    def test_stock_product__should_be_true(self):
        self.store.stock_product(self.soup)
        assert self.soup in self.store.products

    def test_stock_product__should_be_false(self):
        self.store.stock_product(self.soup)
        self.store.stock_product(self.soup)
        assert len(self.store.products) == 1
        assert self.soup == self.store.products[0]

    def test_stock_products__should_stock_store_from_database(self):
        self.store.stock_products()
        assert len(self.store.products) == 5

    def test_discontinue_product__soup_should_no_longer_be_available(self):
        self.store.products = [self.soup, self.beef]
        self.store.discontinue_product(self.soup)
        assert len(self.store.products) == 1
        assert self.soup not in self.store.products

    def test_discontinue_product__store_should_only_have_beef_in_products(self):
        self.store.products = [self.beef]
        self.store.discontinue_product(self.soup)
        assert len(self.store.products) == 1
        assert self.soup not in self.store.products

    @patch('src.models.store.get_special')
    def test_activate_special_on_product__should_assign_special_for_product(self, mock_special):
        self.store.products = [self.soup]
        special_details = {'specialType': 'basic unit discount', 'perUnitDiscount': 0.20, 'limit': 5}
        mock_special.return_value = special_details
        self.store.activate_special_on_product(self.soup)
        assert self.soup.name == mock_special.mock_calls[0][1][0]
        assert self.store.products[0].special_details == special_details
        assert self.store.products[0].has_special is True
