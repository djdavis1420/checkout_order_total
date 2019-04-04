from src.models.cart import Cart
from src.models.product import Product


class Test:

    def setup_method(self):
        self.cart = Cart()
        self.soup = Product('soup', 1.89)

    def test_add_product__should_add_one_soup_to_cart(self):
        self.cart.add_product(self.soup, 1)
        actual = self.cart.products
        assert len(actual) == 1

    def test_add_product__should_add_three_soups_to_cart(self):
        self.cart.add_product(self.soup, 3)
        actual = self.cart.products
        assert len(actual) == 3

    def test_remove_product__should_remove_one_soup_from_cart_leaving_two(self):
        self.cart.add_product(self.soup, 3)
        self.cart.remove_product(self.soup, 1)
        actual = self.cart.products
        assert len(actual) == 2

    def test_remove_product__should_remove_two_soups_from_cart_leaving_one(self):
        self.cart.add_product(self.soup, 3)
        self.cart.remove_product(self.soup, 2)
        actual = self.cart.products
        assert len(actual) == 1
