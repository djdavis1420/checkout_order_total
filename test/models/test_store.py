from src.models.store import Store
from src.models.product import Product


class Test:

    def setup_method(self):
        self.store = Store()
        self.soup = Product('soup', 1.89)
        self.beef = Product('beef', 5.99)

    def test_is_product_available__should_be_false(self):
        actual = self.store.is_product_available(self.soup)
        assert actual is False

    def test_is_product_available__should_be_true(self):
        self.store.stock_product(self.soup)
        actual = self.store.is_product_available(self.soup)
        assert actual is True

    def test_stock_product__should_be_true(self):
        self.store.stock_product(self.soup)
        assert self.soup in self.store.products

    def test_stock_product__should_be_false(self):
        assert self.soup not in self.store.products

    def test_discontinue_product__soup_should_no_longer_be_available(self):
        self.store.stock_product(self.soup)
        self.store.stock_product(self.beef)
        self.store.discontinue_product(self.soup)
        actual = self.store.products
        assert self.soup not in actual

    def test_activate_special_on_product__should_add_special_type_to_product(self):
        self.store.stock_product(self.soup)
        self.store.stock_product(self.beef)
        special_type = 'basic unit discount'
        self.store.activate_special_on_product(self.soup, special_type)
        assert self.soup.special_type == 'basic unit discount'
        assert self.beef.special_type is False
